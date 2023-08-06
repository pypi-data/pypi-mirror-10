from __future__ import division

import pandas as pd
import numpy as np
from functools import wraps, partial
import re
import struct
import os
from glob import glob
from math import ceil
from toolz import merge, dissoc
from itertools import count
from operator import getitem

from ..compatibility import StringIO, unicode, range
from ..utils import textblock

from . import core
from .core import DataFrame, compute, concat, categorize_block, tokens
from .shuffle import set_partition


def _StringIO(data):
    if isinstance(data, bytes):
        data = data.decode()
    return StringIO(data)


def file_size(fn, compression=None):
    """ Size of a file on disk

    If compressed then return the uncompressed file size
    """
    if compression == 'gzip':
        with open(fn, 'rb') as f:
            f.seek(-4, 2)
            result = struct.unpack('I', f.read(4))[0]
    else:
        result = os.stat(fn).st_size
    return result


csv_defaults = {'compression': None}

def fill_kwargs(fn, args, kwargs):
    """ Read a csv file and fill up kwargs

    This normalizes kwargs against a sample file.  It does the following:

    1.  If given a globstring, just use one file
    2.  Get names from csv file if not given
    3.  Identify the presence of a header
    4.  Identify dtypes
    5.  Establish column names
    6.  Switch around dtypes and column names if parse_dates is active

    Normally ``pd.read_csv`` does this for us.  However for ``dd.read_csv`` we
    need to be consistent across multiple files and don't want to do these
    heuristics each time so we use the pandas solution once, record the
    results, and then send back a fully explicit kwargs dict to send to future
    calls to ``pd.read_csv``.

    Returns
    -------

    kwargs: dict
        keyword arguments to give to pd.read_csv
    """
    kwargs = merge(csv_defaults, kwargs)
    sample_nrows = kwargs.pop('sample_nrows', 1000)
    essentials = ['columns', 'names', 'header', 'parse_dates', 'dtype']
    if set(essentials).issubset(kwargs):
        return kwargs

    # Let pandas infer on the first 100 rows
    if '*' in fn:
        fn = sorted(glob(fn))[0]

    if 'names' not in kwargs:
        kwargs['names'] = csv_names(fn, **kwargs)
    if 'header' not in kwargs:
        kwargs['header'] = infer_header(fn, **kwargs)
        if kwargs['header'] is True:
            kwargs['header'] = 0

    try:
        head = pd.read_csv(fn, *args, nrows=sample_nrows, **kwargs)
    except StopIteration:
        head = pd.read_csv(fn, *args, **kwargs)

    if 'parse_dates' not in kwargs:
        kwargs['parse_dates'] = [col for col in head.dtypes.index
                           if np.issubdtype(head.dtypes[col], np.datetime64)]
    if 'dtype' not in kwargs:
        kwargs['dtype'] = dict(head.dtypes)
        for col in kwargs['parse_dates']:
            del kwargs['dtype'][col]

    kwargs['columns'] = list(head.columns)

    return kwargs

@wraps(pd.read_csv)
def read_csv(fn, *args, **kwargs):
    chunkbytes = kwargs.pop('chunkbytes', 2**25)  # 50 MB
    categorize = kwargs.pop('categorize', None)
    index = kwargs.pop('index', None)
    if index and categorize == None:
        categorize = True

    kwargs = fill_kwargs(fn, args, kwargs)

    # Handle glob strings
    if '*' in fn:
        return concat([read_csv(f, *args, **kwargs) for f in sorted(glob(fn))])

    columns = kwargs.pop('columns')

    # Chunk sizes and numbers
    total_bytes = file_size(fn, kwargs['compression'])
    nchunks = int(ceil(total_bytes / chunkbytes))
    divisions = [None] * (nchunks + 1)

    header = kwargs.pop('header')

    first_read_csv = partial(pd.read_csv, *args, header=header,
                           **dissoc(kwargs, 'compression'))
    rest_read_csv = partial(pd.read_csv, *args, header=None,
                          **dissoc(kwargs, 'compression'))

    # Create dask graph
    name = 'read-csv' + next(tokens)
    dsk = dict(((name, i), (rest_read_csv, (_StringIO,
                               (textblock, fn,
                                   i*chunkbytes, (i+1) * chunkbytes,
                                   kwargs['compression']))))
               for i in range(1, nchunks))
    dsk[(name, 0)] = (first_read_csv, (_StringIO,
                       (textblock, fn, 0, chunkbytes, kwargs['compression'])))

    result = DataFrame(dsk, name, columns, divisions)

    if categorize or index:
        categories, quantiles = categories_and_quantiles(fn, args, kwargs,
                                                         index, categorize,
                                                         chunkbytes=chunkbytes)

    if categorize:
        func = partial(categorize_block, categories=categories)
        result = result.map_partitions(func, columns=columns)

    if index:
        result = set_partition(result, index, quantiles)

    return result


def infer_header(fn, encoding='utf-8', compression=None, **kwargs):
    """ Guess if csv file has a header or not

    This uses Pandas to read a sample of the file, then looks at the column
    names to see if they are all word-like.

    Returns True or False
    """
    # See read_csv docs for header for reasoning
    try:
        df = pd.read_csv(fn, encoding=encoding, compression=compression,nrows=5)
    except StopIteration:
        df = pd.read_csv(fn, encoding=encoding, compression=compression)
    return (len(df) > 0 and
            all(re.match('^\s*\D\w*\s*$', n) for n in df.columns) and
            not all(dt == 'O' for dt in df.dtypes))


def csv_names(fn, encoding='utf-8', compression=None, names=None,
                parse_dates=None, usecols=None, dtype=None, **kwargs):
    try:
        df = pd.read_csv(fn, encoding=encoding, compression=compression,
                names=names, parse_dates=parse_dates, nrows=5, **kwargs)
    except StopIteration:
        df = pd.read_csv(fn, encoding=encoding, compression=compression,
                names=names, parse_dates=parse_dates, **kwargs)
    return list(df.columns)


def categories_and_quantiles(fn, args, kwargs, index=None, categorize=None,
        chunkbytes=2**26):
    """
    Categories of Object columns and quantiles of index column for CSV

    Computes both of the following in a single pass

    1.  The categories for all object dtype columns
    2.  The quantiles of the index column

    Parameters
    ----------

    fn: string
        Filename of csv file
    args: tuple
        arguments to be passed in to read_csv function
    kwargs: dict
        keyword arguments to pass in to read_csv function
    index: string or None
        Name of column on which to compute quantiles
    categorize: bool
        Whether or not to compute categories of Object dtype columns
    """
    kwargs = kwargs.copy()

    compression = kwargs.get('compression', None)
    total_bytes = file_size(fn, compression)
    nchunks = int(ceil(total_bytes / chunkbytes))

    if infer_header(fn, **kwargs):
        kwargs['header'] = 0

    one_chunk = pd.read_csv(fn, *args, nrows=100, **kwargs)

    if categorize is not False:
        category_columns = [c for c in one_chunk.dtypes.index
                               if one_chunk.dtypes[c] == 'O'
                               and c not in kwargs.get('parse_dates', ())]
    else:
        category_columns = []
    cols = category_columns + ([index] if index else [])

    dtypes = dict((c, one_chunk.dtypes[c]) for c in cols)
    d = read_csv(fn, *args, **merge(kwargs,
                                    dict(usecols=cols,
                                         parse_dates=None,
                                         dtype=dtypes)))
    categories = [d[c].drop_duplicates() for c in category_columns]

    import dask
    if index:
        quantiles = d[index].quantiles(np.linspace(0, 100, nchunks + 1))
        result = compute(quantiles, *categories)
        quantiles, categories = result[0], result[1:]
    else:
        categories = compute(*categories)
        quantiles = None

    categories = dict(zip(category_columns, categories))

    return categories, quantiles


def from_array(x, chunksize=50000):
    """ Read dask Dataframe from any slicable array with record dtype

    Uses getitem syntax to pull slices out of the array.  The array need not be
    a NumPy array but must support slicing syntax

        x[50000:100000]

    and have a record dtype

        x.dtype == [('name', 'O'), ('balance', 'i8')]

    """
    columns = tuple(x.dtype.names)
    divisions = tuple(range(0, len(x), chunksize))
    if divisions[-1] != len(x) - 1:
        divisions = divisions + (len(x) - 1,)
    name = 'from_array' + next(tokens)
    dsk = dict(((name, i), (pd.DataFrame,
                             (getitem, x,
                              slice(i * chunksize, (i + 1) * chunksize))))
            for i in range(0, int(ceil(len(x) / chunksize))))

    return DataFrame(dsk, name, columns, divisions)


def from_pandas(data, npartitions):
    """Construct a dask object from a pandas object.

    If given a ``pandas.Series`` a ``dask.Series`` will be returned. If given a
    ``pandas.DataFrame`` a ``dask.DataFrame`` will be returned. All other
    pandas objects will raise a ``TypeError``.

    Parameters
    ----------
    df : pandas.DataFrame or pandas.Series
        The DataFrame/Series with which to construct a dask DataFrame/Series
    npartitions : int
        The number of partitions of the index to create

    Returns
    -------
    dask.DataFrame or dask.Series
        A dask DataFrame/Series partitioned along the index

    Examples
    --------
    >>> df = pd.DataFrame(dict(a=list('aabbcc'), b=list(range(6))),
    ...                   index=pd.date_range(start='20100101', periods=6))
    >>> ddf = from_pandas(df, npartitions=3)
    >>> ddf.divisions  # doctest: +NORMALIZE_WHITESPACE
    (Timestamp('2010-01-01 00:00:00', offset='D'),
     Timestamp('2010-01-03 00:00:00', offset='D'),
     Timestamp('2010-01-05 00:00:00', offset='D'),
     Timestamp('2010-01-06 00:00:00', offset='D'))
    >>> ddf = from_pandas(df.a, npartitions=3)  # Works with Series too!
    >>> ddf.divisions  # doctest: +NORMALIZE_WHITESPACE
    (Timestamp('2010-01-01 00:00:00', offset='D'),
     Timestamp('2010-01-03 00:00:00', offset='D'),
     Timestamp('2010-01-05 00:00:00', offset='D'),
     Timestamp('2010-01-06 00:00:00', offset='D'))

    Raises
    ------
    TypeError
        If something other than a ``pandas.DataFrame`` or ``pandas.Series`` is
        passed in.

    See Also
    --------
    from_array : Construct a dask.DataFrame from an array that has record dtype
    from_bcolz : Construct a dask.DataFrame from a bcolz ctable
    read_csv : Construct a dask.DataFrame from a CSV file
    """
    columns = getattr(data, 'columns', getattr(data, 'name', None))
    if columns is None and not isinstance(data, pd.Series):
        raise TypeError("Input must be a pandas DataFrame or Series")
    nrows = len(data)
    chunksize = int(ceil(nrows / npartitions))
    data = data.sort_index(ascending=True)
    divisions = tuple(data.index[i]
                      for i in range(0, nrows, chunksize))
    divisions = divisions + (data.index[-1],)
    name = 'from_pandas' + next(tokens)
    dsk = dict(((name, i), data.iloc[i * chunksize:(i + 1) * chunksize])
               for i in range(npartitions - 1))
    dsk[(name, npartitions - 1)] = data.iloc[chunksize*(npartitions - 1):]
    return getattr(core, type(data).__name__)(dsk, name, columns, divisions)


def from_bcolz(x, chunksize=None, categorize=True, index=None, **kwargs):
    """ Read dask Dataframe from bcolz.ctable

    Parameters
    ----------

    x : bcolz.ctable
        Input data
    chunksize : int (optional)
        The size of blocks to pull out from ctable.  Ideally as large as can
        comfortably fit in memory
    categorize : bool (defaults to True)
        Automatically categorize all string dtypes
    index : string (optional)
        Column to make the index

    See Also
    --------

    from_array: more generic function not optimized for bcolz
    """
    import dask.array as da
    import bcolz
    if isinstance(x, (str, unicode)):
        x = bcolz.ctable(rootdir=x)
    bc_chunklen = max(x[name].chunklen for name in x.names)
    if chunksize is None and bc_chunklen > 10000:
        chunksize = bc_chunklen

    categories = dict()
    if categorize:
        for name in x.names:
            if (np.issubdtype(x.dtype[name], np.string_) or
                    np.issubdtype(x.dtype[name], np.unicode_) or
                    np.issubdtype(x.dtype[name], np.object_)):
                a = da.from_array(x[name], chunks=(chunksize * len(x.names),))
                categories[name] = da.unique(a)

    columns = tuple(x.dtype.names)
    divisions = (0,) + tuple(range(-1, len(x), chunksize))[1:]
    if divisions[-1] != len(x) - 1:
        divisions = divisions + (len(x) - 1,)
    new_name = 'from_bcolz' + next(tokens)
    dsk = dict(((new_name, i),
                (dataframe_from_ctable,
                 x,
                 (slice(i * chunksize, (i + 1) * chunksize),),
                 None, categories))
               for i in range(0, int(ceil(len(x) / chunksize))))

    result = DataFrame(dsk, new_name, columns, divisions)

    if index:
        assert index in x.names
        a = da.from_array(x[index], chunks=(chunksize * len(x.names),))
        q = np.linspace(0, 100, len(x) // chunksize + 2)
        divisions = da.percentile(a, q).compute()
        return set_partition(result, index, divisions, **kwargs)
    else:
        return result


def dataframe_from_ctable(x, slc, columns=None, categories=None):
    """ Get DataFrame from bcolz.ctable

    Parameters
    ----------

    x: bcolz.ctable
    slc: slice
    columns: list of column names or None

    >>> import bcolz
    >>> x = bcolz.ctable([[1, 2, 3, 4], [10, 20, 30, 40]], names=['a', 'b'])
    >>> dataframe_from_ctable(x, slice(1, 3))
       a   b
    0  2  20
    1  3  30

    >>> dataframe_from_ctable(x, slice(1, 3), columns=['b'])
        b
    0  20
    1  30

    >>> dataframe_from_ctable(x, slice(1, 3), columns='b')
    0    20
    1    30
    Name: b, dtype: int64

    """
    import bcolz
    if columns is not None:
        if isinstance(columns, tuple):
            columns = list(columns)
        x = x[columns]

    name = 'from-bcolz' + next(tokens)

    if isinstance(x, bcolz.ctable):
        chunks = [x[name][slc] for name in x.names]
        if categories is not None:
            chunks = [pd.Categorical.from_codes(np.searchsorted(categories[name],
                                                                chunk),
                                                categories[name], True)
                       if name in categories else chunk
                       for name, chunk in zip(x.names, chunks)]
        return pd.DataFrame(dict(zip(x.names, chunks)))
    elif isinstance(x, bcolz.carray):
        chunk = x[slc]
        if categories is not None and columns and columns in categories:
            chunk = pd.Categorical.from_codes(
                        np.searchsorted(categories[columns], chunk),
                        categories[columns], True)
        return pd.Series(chunk, name=columns)
