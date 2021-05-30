#!/usr/bin/env python

from m1_scrip2 import *


class Script1:
    @staticmethod
    def Say_Hi():
        print('Hello from <<script1>> -> module1')


if __name__ == '__main__':
    X = Script2.Say_Hi()
