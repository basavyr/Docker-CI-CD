#!/usr/bin/env python

import module1.m1_scrip1 as m1
import module1.m1_scrip2 as m2

# import sys
# sys.path.append('module1/')


def Main():
    x=m2.Script2.ClassFunction(m1.Script1.ARGX)
    print(x)


if __name__ == '__main__':
    Main()
