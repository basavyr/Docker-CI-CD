#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy.random as rd
import numpy as np

fig = 'dockerized_plot.pdf'


class Functions:
    def function1(self, arg):
        return arg * arg + 1

    def function2(self, arg, a):
        return a * arg * arg + 1

    def function3(self, arg, a):
        with np.errstate(divide='ignore'):
            x = a * np.log(arg) + np.sin(arg)
        return x


x1 = np.arange(0, 3, 0.1)


a1 = rd.choice([1, 2, 4])
a2 = rd.choice([1, 2, 3])


def make_plot(a1, a2):
    print('Starts the plotting procedure')
    print(f'a1 -> {a1}')
    print(f'a2 -> {a2}')

    plt.plot(x1, list(map(Functions().function1, x1)), '-or', label='f1')
    plt.plot(x1, list(map(Functions().function2, x1,
                          [a1 for x in x1])), '-og', label='f2')
    plt.plot(x1, list(map(Functions().function3, x1,
                          [a2 for x in x1])), '-ob', label='f3')
    plt.legend(loc='best')
    plt.savefig(fig, bbox_inches='tight', dpi=300)

    print('Finishing the plotting procedure')
    print(f'Plot saved at -> {fig}')


make_plot(a1, a2)
