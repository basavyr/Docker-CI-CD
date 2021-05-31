#!/usr/bin/env python

try:
    import m1_scrip2
except ImportError:
    from . import m1_scrip2


class Script1:
    @staticmethod
    def Say_Hi():
        print('Hello from <<script1>> -> module1')


def Main():
    Script1.Say_Hi()
    m1_scrip2.Script2.Say_Hi()


if __name__ == '__main__':
    Main()
