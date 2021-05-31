#!/usr/bin/env python

import m1_scrip1


class Script2:
    @staticmethod
    def Say_Hi():
        print('Hello from <<script2>> -> module1')


if __name__ == '__main__':
    X = m1_scrip1.Script1.Say_Hi()
