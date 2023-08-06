import pytest
pytest.importorskip('numpy')

import numpy as np
import dill
from dask.array.core import Array
from dask.array.random import random, exponential, normal
import dask.array as da
import dask
from dask.multiprocessing import get as mpget


def test_RandomState():
    state = da.random.RandomState(5)
    x = state.normal(10, 1, size=10, chunks=5)
    assert (x.compute() == x.compute()).all()

    state = da.random.RandomState(5)
    y = state.normal(10, 1, size=10, chunks=5)
    assert (x.compute() == y.compute()).all()


def test_concurrency():
    state = da.random.RandomState(5)
    x = state.normal(10, 1, size=10, chunks=2)

    state = da.random.RandomState(5)
    y = state.normal(10, 1, size=10, chunks=2)
    assert (x.compute(get=mpget) == y.compute(get=mpget)).all()


def test_doc_randomstate():
    assert 'mean' in da.random.RandomState(5).normal.__doc__


def test_serializability():
    state = da.random.RandomState(5)
    x = state.normal(10, 1, size=10, chunks=5)

    y = dill.loads(dill.dumps(x))

    assert (x.compute() == y.compute()).all()


def test_determinisim_through_dask_values():
    samples_1 = da.random.RandomState(42).normal(size=1000, chunks=10)
    samples_2 = da.random.RandomState(42).normal(size=1000, chunks=10)

    assert [v for k, v in sorted(samples_1.dask.items())] ==\
           [v for k, v in sorted(samples_2.dask.items())]


def test_random():
    a = random((10, 10), chunks=(5, 5))
    assert isinstance(a, Array)
    assert isinstance(a.name, str) and a.name
    assert a.shape == (10, 10)
    assert a.chunks == ((5, 5), (5, 5))

    x = set(np.array(a).flat)

    assert len(x) > 90


def test_parametrized_random_function():
    a = exponential(1000, (10, 10), chunks=(5, 5))
    assert isinstance(a, Array)
    assert isinstance(a.name, str) and a.name
    assert a.shape == (10, 10)
    assert a.chunks == ((5, 5), (5, 5))

    x = np.array(a)
    assert 10 < x.mean() < 100000

    y = set(x.flat)
    assert len(y) > 90


def test_kwargs():
    a = normal(loc=10.0, scale=0.1, size=(10, 10), chunks=(5, 5))
    assert isinstance(a, Array)
    x = np.array(a)
    assert 8 < x.mean() < 12


def test_unique_names():
    a = random((10, 10), chunks=(5, 5))
    b = random((10, 10), chunks=(5, 5))

    assert a.name != b.name


def test_docs():
    assert 'exponential' in exponential.__doc__
    assert 'exponential' in exponential.__name__


def test_can_make_really_big_random_array():
    x = normal(10, 1, (1000000, 1000000), chunks=(100000, 100000))
