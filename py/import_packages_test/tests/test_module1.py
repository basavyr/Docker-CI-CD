#!/usr/bin/env python

import sys

try:
    sys.path.append('module1/')
    from .module import m1_scrip1
    from .module import m1_scrip2
except ImportError:
    sys.path.append('../')
    from module1 import m1_scrip1
    from module1 import m1_scrip2


m1_scrip2.Main()
print(m1_scrip1.Script1.ARGX)
