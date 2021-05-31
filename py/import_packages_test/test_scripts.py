#!/usr/bin/env python
# from module1 import m1_scrip1
# from module1 import m1_scrip2

# m1_scrip1.Script1.Say_Hi()
# m1_scrip2.Script2.Say_Hi()


import sys
sys.path.append('module1/')

import m1_scrip2 as m12
import m1_scrip1 as m11

m11.Script1.Say_Hi()
m12.Script2.Say_Hi()
