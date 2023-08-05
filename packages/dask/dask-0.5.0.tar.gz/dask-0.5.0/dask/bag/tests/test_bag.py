from __future__ import absolute_import, division, print_function

import pytest
pytest.importorskip('dill')

from toolz import (merge, join, pipe, filter, identity, merge_with, take,
        partial)
import math
from dask.bag.core import (Bag, lazify, lazify_task, fuse, map, collect,
        reduceby, bz2_stream)
from dask.utils import filetexts
import dask
from pbag import PBag
import dask.bag as db
import shutil
import os
import gzip
import bz2
from dask.utils import raises

from collections import Iterator

dsk = {('x', 0): (range, 5),
       ('x', 1): (range, 5),
       ('x', 2): (range, 5)}

L = list(range(5)) * 3

b = Bag(dsk, 'x', 3)

def inc(x):
    return x + 1

def iseven(x):
    return x % 2 == 0

def isodd(x):
    return x % 2 == 1

def add(x, y):
    return x + y


def test_Bag():
    assert b.name == 'x'
    assert b.npartitions == 3


def test_keys():
    assert sorted(b._keys()) == sorted(dsk.keys())


def test_map():
    c = b.map(inc)
    expected = merge(dsk, dict(((c.name, i), (list, (map, inc, (b.name, i))))
                               for i in range(b.npartitions)))
    assert c.dask == expected


def test_map_function_with_multiple_arguments():
    b = db.from_sequence([(1, 10), (2, 20), (3, 30)], npartitions=3)
    assert list(b.map(lambda x, y: x + y)) == [11, 22, 33]


def test_filter():
    c = b.filter(iseven)
    expected = merge(dsk, dict(((c.name, i),
                                (list, (filter, iseven, (b.name, i))))
                               for i in range(b.npartitions)))
    assert c.dask == expected


def test_iter():
    assert sorted(list(b)) == sorted(L)
    assert sorted(list(b.map(inc))) == sorted(list(range(1, 6)) * 3)


def test_pluck():
    d = {('x', 0): [(1, 10), (2, 20)],
         ('x', 1): [(3, 30), (4, 40)]}
    b = Bag(d, 'x', 2)
    assert set(b.pluck(0)) == set([1, 2, 3, 4])
    assert set(b.pluck(1)) == set([10, 20, 30, 40])
    assert set(b.pluck([1, 0])) == set([(10, 1), (20, 2), (30, 3), (40, 4)])


def test_pluck_with_default():
    b = db.from_sequence(['Hello', '', 'World'])
    assert raises(IndexError, lambda: list(b.pluck(0)))
    assert list(b.pluck(0, None)) == ['H', None, 'W']


def test_fold_computation():
    assert int(b.fold(add)) == sum(L)


def test_distinct():
    assert sorted(b.distinct()) == [0, 1, 2, 3, 4]


def test_frequencies():
    assert dict(list(b.frequencies())) == {0: 3, 1: 3, 2: 3, 3: 3, 4: 3}


def test_topk():
    assert list(b.topk(4)) == [4, 4, 4, 3]
    assert list(b.topk(4, key=lambda x: -x)) == [0, 0, 0, 1]


def test_lambdas():
    assert list(b.map(lambda x: x + 1)) == list(b.map(inc))

def test_reductions():
    assert int(b.count()) == 15
    assert int(b.sum()) == 30
    assert int(b.max()) == 4
    assert int(b.min()) == 0
    assert int(b.any()) == True
    assert int(b.all()) == False  # some zeros exist

def test_mean():
    assert float(b.mean()) == 2.0

def test_std():
    assert float(b.std()) == math.sqrt(2.0)

def test_var():
    assert float(b.var()) == 2.0


def test_join():
    assert list(b.join([1, 2, 3], on_self=isodd, on_other=iseven)) == \
            list(join(iseven, [1, 2, 3], isodd, list(b)))
    assert list(b.join([1, 2, 3], isodd)) == \
            list(join(isodd, [1, 2, 3], isodd, list(b)))

def test_foldby():
    c = b.foldby(iseven, add, 0, add, 0)
    assert (reduceby, iseven, add, (b.name, 0), 0) in list(c.dask.values())
    assert set(c) == set(reduceby(iseven, lambda acc, x: acc + x, L, 0).items())

    c = b.foldby(iseven, lambda acc, x: acc + x)
    assert set(c) == set(reduceby(iseven, lambda acc, x: acc + x, L, 0).items())


def test_map_partitions():
    assert list(b.map_partitions(len)) == [5, 5, 5]


def test_lazify_task():
    task = (sum, (list, (map, inc, [1, 2, 3])))
    assert lazify_task(task) == (sum, (map, inc, [1, 2, 3]))

    task = (list, (map, inc, [1, 2, 3]))
    assert lazify_task(task) == task

    a = (list, (map, inc,
                     (list, (filter, iseven, 'y'))))
    b = (list, (map, inc,
                            (filter, iseven, 'y')))
    assert lazify_task(a) == b


f = lambda x: x


def test_lazify():
    a = {'x': (list, (map, inc,
                           (list, (filter, iseven, 'y')))),
         'a': (f, 'x'), 'b': (f, 'x')}
    b = {'x': (list, (map, inc,
                                  (filter, iseven, 'y'))),
         'a': (f, 'x'), 'b': (f, 'x')}
    assert lazify(a) == b


def test_take():
    assert list(b.take(2)) == [0, 1]
    assert b.take(2) == (0, 1)


def test_map_is_lazy():
    from dask.bag.core import map
    assert isinstance(map(lambda x: x, [1, 2, 3]), Iterator)

def test_can_use_dict_to_make_concrete():
    assert isinstance(dict(b.frequencies()), dict)


def test_from_filenames():
    with filetexts({'a1.log': 'A\nB', 'a2.log': 'C\nD'}) as fns:
        assert set(line.strip() for line in db.from_filenames(fns)) == \
                set('ABCD')
        assert set(line.strip() for line in db.from_filenames('a*.log')) == \
                set('ABCD')


def test_from_filenames_gzip():
    b = db.from_filenames(['foo.json.gz', 'bar.json.gz'])

    assert set(b.dask.values()) == set([(list, (gzip.open, 'foo.json.gz')),
                                        (list, (gzip.open, 'bar.json.gz'))])


def test_from_filenames_bz2():
    b = db.from_filenames(['foo.json.bz2', 'bar.json.bz2'])

    assert set(b.dask.values()) == set([(list, (bz2.BZ2File, 'foo.json.bz2')),
                                        (list, (bz2.BZ2File, 'bar.json.bz2'))])


def test_from_sequence():
    b = db.from_sequence([1, 2, 3, 4, 5], npartitions=3)
    assert len(b.dask) == 3
    assert set(b) == set([1, 2, 3, 4, 5])


def test_from_long_sequence():
    L = list(range(1001))
    b = db.from_sequence(L)
    assert set(b) == set(L)


def test_product():
    b2 = b.product(b)
    assert b2.npartitions == b.npartitions**2
    assert set(b2) == set([(i, j) for i in L for j in L])

    x = db.from_sequence([1, 2, 3, 4])
    y = db.from_sequence([10, 20, 30])
    z = x.product(y)
    assert set(z) == set([(i, j) for i in [1, 2, 3, 4] for j in [10, 20, 30]])


def test_collect():
    a = PBag(identity, 2)
    with a:
        a.extend([0, 1, 2, 3])

    b = PBag(identity, 2)
    with b:
        b.extend([0, 1, 2, 3])

    result = merge(dict(collect(identity, 2, 0, [a, b])),
                   dict(collect(identity, 2, 1, [a, b])))

    assert result == {0: [0, 0],
                      1: [1, 1],
                      2: [2, 2],
                      3: [3, 3]}


def test_groupby():
    result = dict(b.groupby(lambda x: x))
    assert result == {0: [0, 0 ,0],
                      1: [1, 1, 1],
                      2: [2, 2, 2],
                      3: [3, 3, 3],
                      4: [4, 4, 4]}
    assert b.groupby(lambda x: x).npartitions == b.npartitions


def test_groupby_with_indexer():
    b = db.from_sequence([[1, 2, 3], [1, 4, 9], [2, 3, 4]])
    result = dict(b.groupby(0))
    assert result == {1: [[1, 2, 3], [1, 4, 9]],
                      2: [[2, 3, 4]]}

def test_groupby_with_npartitions_changed():
    result = b.groupby(lambda x: x, npartitions=1)
    assert dict(result) == {0: [0, 0 ,0],
                            1: [1, 1, 1],
                            2: [2, 2, 2],
                            3: [3, 3, 3],
                            4: [4, 4, 4]}

    assert result.npartitions == 1

def test_concat():
    b = db.from_sequence([1, 2, 3]).map(lambda x: x * [1, 2, 3])
    assert list(b.concat()) == [1, 2, 3] * sum([1, 2, 3])


def test_args():
    c = b.map(lambda x: x + 1)
    d = Bag(*c._args)

    assert list(c) == list(d)
    assert c.npartitions == d.npartitions


def test_to_dataframe():
    try:
        import dask.dataframe
    except ImportError:
        return
    b = db.from_sequence([(1, 2), (10, 20), (100, 200)], npartitions=2)
    df = b.to_dataframe(columns=['a', 'b'])
    assert df.npartitions == b.npartitions
    assert list(df.columns) == ['a', 'b']

    assert df.a.compute().values.tolist() == list(b.pluck(0))
    assert df.b.compute().values.tolist() == list(b.pluck(1))

    b = db.from_sequence([{'a':   1, 'b':   2},
                          {'a':  10, 'b':  20},
                          {'a': 100, 'b': 200}], npartitions=2)

    df2 = b.to_dataframe()

    assert (df2.compute().values == df.compute().values).all()

def test_to_textfiles():
    b = db.from_sequence(['abc', '123', 'xyz'], npartitions=2)
    for ext, myopen in [('gz', gzip.open), ('bz2', bz2.BZ2File), ('', open)]:
        c = b.to_textfiles('_foo/*.' + ext)
        assert c.npartitions == b.npartitions
        try:
            c.compute(get=dask.get)
            assert os.path.exists('_foo/1.' + ext)

            f = myopen('_foo/1.' + ext, 'r')
            text = f.read()
            if hasattr(text, 'decode'):
                text = text.decode()
            assert 'xyz' in text
            f.close()
        finally:
            shutil.rmtree('_foo')


def test_bz2_stream():
    text = '\n'.join(map(str, range(10000)))
    compressed = bz2.compress(text.encode())
    assert list(take(100, bz2_stream(compressed))) == list(map(str, range(100)))


def test_concat():
    a = db.from_sequence([1, 2, 3])
    b = db.from_sequence([4, 5, 6])
    c = db.concat([a, b])

    assert list(c) == [1, 2, 3, 4, 5, 6]


def test_string_namespace():
    b = db.from_sequence(['Alice Smith', 'Bob Jones', 'Charlie Smith'],
                         npartitions=2)

    assert 'split' in dir(b.str)
    assert 'match' in dir(b.str)

    assert list(b.str.lower()) == ['alice smith', 'bob jones', 'charlie smith']
    assert list(b.str.split(' ')) == [['Alice', 'Smith'],
                                      ['Bob', 'Jones'],
                                      ['Charlie', 'Smith']]
    assert list(b.str.match('*Smith')) == ['Alice Smith', 'Charlie Smith']
