from __future__ import absolute_import, division, print_function

from collections import Iterator
from contextlib import contextmanager
import os
import gzip
import tempfile

from .compatibility import unicode

def raises(err, lamda):
    try:
        lamda()
        return False
    except err:
        return True


def deepmap(func, *seqs):
    """ Apply function inside nested lists

    >>> inc = lambda x: x + 1
    >>> deepmap(inc, [[1, 2], [3, 4]])
    [[2, 3], [4, 5]]

    >>> add = lambda x, y: x + y
    >>> deepmap(add, [[1, 2], [3, 4]], [[10, 20], [30, 40]])
    [[11, 22], [33, 44]]
    """
    if isinstance(seqs[0], (list, Iterator)):
        return [deepmap(func, *items) for items in zip(*seqs)]
    else:
        return func(*seqs)


@contextmanager
def ignoring(*exceptions):
    try:
        yield
    except exceptions:
        pass


@contextmanager
def tmpfile(extension=''):
    extension = '.' + extension.lstrip('.')
    handle, filename = tempfile.mkstemp(extension)
    os.close(handle)
    os.remove(filename)

    try:
        yield filename
    finally:
        if os.path.exists(filename):
            if os.path.isdir(filename):
                shutil.rmtree(filename)
            else:
                os.remove(filename)


@contextmanager
def filetext(text, extension='', open=open, mode='w'):
    with tmpfile(extension=extension) as filename:
        f = open(filename, mode=mode)
        try:
            f.write(text)
        finally:
            try:
                f.close()
            except AttributeError:
                pass

        yield filename


def repr_long_list(seq):
    """

    >>> repr_long_list(list(range(100)))
    '[0, 1, 2, ..., 98, 99]'
    """
    if len(seq) < 8:
        return repr(seq)
    else:
        return repr(seq[:3])[:-1] + ', ..., ' + repr(seq[-2:])[1:]


class IndexCallable(object):
    """ Provide getitem syntax for functions

    >>> def inc(x):
    ...     return x + 1

    >>> I = IndexCallable(inc)
    >>> I[3]
    4
    """
    __slots__ = 'fn',
    def __init__(self, fn):
        self.fn = fn

    def __getitem__(self, key):
        return self.fn(key)


@contextmanager
def filetexts(d, open=open):
    """ Dumps a number of textfiles to disk

    d - dict
        a mapping from filename to text like {'a.csv': '1,1\n2,2'}
    """
    for filename, text in d.items():
        f = open(filename, 'wt')
        try:
            f.write(text)
        finally:
            try:
                f.close()
            except AttributeError:
                pass

    yield list(d)

    for filename in d:
        if os.path.exists(filename):
            os.remove(filename)


opens = {'gzip': gzip.open}


def textblock(file, start, stop, compression=None):
    """ Pull out a block of text from a file given start and stop bytes

    This gets data starting/ending from the next newline delimiter

    Example
    -------

    >> with open('myfile.txt', 'w') as f:
    ..     f.write('123\n456\n789\nabc')

    >> f = open('myfile.txt')

    In the example below, 1 and 10 don't line up with endlines

    >> textblock(f, 1, 10)
    '456\n789\n'
    """
    if isinstance(file, (str, unicode)):
        myopen = opens.get(compression, open)
        f = myopen(file, 'rb')
        try:
            result = textblock(f, start, stop)
        finally:
            f.close()
        return result
    if start:
        file.seek(start - 1)
        line = file.readline() # burn a line
        start = file.tell()

    if stop is None:
        file.seek(start)
        return file.read()

    stop -= 1
    file.seek(stop)
    line = file.readline()
    stop = file.tell()

    file.seek(start)

    return file.read(stop - start)
