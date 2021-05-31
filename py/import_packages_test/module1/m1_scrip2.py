#!/usr/bin/env python

try:
    import m1_scrip1
except ImportError:
    from . import m1_scrip1


class Script2:
    @staticmethod
    def Say_Hi():
        print('Hello from <<script2>> -> module1')

    @classmethod
    def ClassFunction(cls, argument):
        return f'This is the function -> <<{Script2.ClassFunction.__name__}>>\nThis is the argument {argument}'


def Main():
    Script2.Say_Hi()
    m1_scrip1.Script1.Say_Hi()


if __name__ == '__main__':
    Main()
