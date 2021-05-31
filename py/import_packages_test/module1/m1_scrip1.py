#!/usr/bin/env python

import m1_scrip2
class Script1:
    @staticmethod
    def Say_Hi():
        print('Hello from <<script1>> -> module1')


if __name__ == '__main__':
    X=m1_scrip2.Script2.Say_Hi()
