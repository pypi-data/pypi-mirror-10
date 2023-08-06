import os
from functools import partial

import numpy as np
import pytest

nx = pytest.importorskip("networkx")

from dask.dot import to_networkx, dot_graph, lower


def add(x, y):
    return x + y


def inc(x):
    return x + 1

dsk = {'x': 1, 'y': (inc, 'x'),
       'a': 2, 'b': (inc, 'a'),
       'z': (add, 'y', 'b'),
       'c': (sum, ['y', 'b'])}


def test_to_networkx():
    g = to_networkx(dsk)
    assert isinstance(g, nx.DiGraph)
    assert all(n in g.node for n in ['x', 'a', 'z', 'b', 'y'])


def test_lower():
    assert lower(partial(add, 1)) is add

def test_dot_graph():
    fn = 'test_dot_graph'
    fns = [fn + ext for ext in ['.png', '.pdf', '.dot']]
    try:
        dot_graph(dsk, filename=fn)
        assert all(os.path.exists(f) for f in fns)
    except (ImportError, AttributeError):
        pass
    finally:
        for f in fns:
            if os.path.exists(f):
                os.remove(f)

def test_aliases():
    g = to_networkx({'x': 1, 'y': 'x'})
    assert 'y' in g.edge['x']


def test_np_graph():
    g = to_networkx({'x': np.array([[1, 2]])})
    assert g.node['x']['label'] == 'x=[[1 2]]' 
    
