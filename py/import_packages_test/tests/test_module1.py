#!/usr/bin/env python

import sys
import os
try:
    sys.path.append('../')
    from module1 import m1_scrip1
    from module1 import m1_scrip2
except ImportError:
    print('failed')
    sys.path.append('.')
    from module1 import m1_scrip1
    from module1 import m1_scrip2

m1_scrip2.Main()
print(m1_scrip1.Script1.ARGX)
