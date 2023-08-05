from __future__ import absolute_import, division, print_function

import sys

PY3 = sys.version_info[0] == 3
PY2 = sys.version_info[0] == 2

if PY3:
    import builtins
    from queue import Queue, Empty
    from itertools import zip_longest
    from io import StringIO
    unicode = str
    long = int
    def apply(func, args):
        return func(*args)
else:
    import __builtin__ as builtins
    from Queue import Queue, Empty
    import operator
    from itertools import izip_longest as zip_longest
    from StringIO import StringIO
    unicode = unicode
    long = long
    apply = apply


def skip(func):
    return
