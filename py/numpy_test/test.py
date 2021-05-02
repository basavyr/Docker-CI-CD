#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

fig = 'dockerized_plot.pdf'


class Functions:
    def function1(self, arg):
        return arg * arg + 1

    def function2(self, arg):
        return 2 * arg * arg + 1

    def function3(self, arg):
        with np.errstate(divide='ignore'):
            x = 2 * np.log(arg) + np.sin(arg)
        return x


x1 = np.arange(0, 3, 0.1)

PLOT = 0

if(PLOT):
    print('Starts the plotting procedure')

    plt.plot(x1, list(map(Functions().function1, x1)), '-or', label='f1')
    plt.plot(x1, list(map(Functions().function2, x1)), '-og', label='f2')
    plt.plot(x1, list(map(Functions().function3, x1)), '-ob', label='f3')
    plt.legend(loc='best')
    plt.savefig(fig, bbox_inches='tight', dpi=300)

    print('Finishing the plotting procedure')
    print(f'Plot saved at -> {fig}')


def t_fct(x1, a):
    return x1 + a


x_in = [1, 2, 3]

print(f'{x_in} -> {list(map(t_fct, x_in,[2 for x in x_in]))}')
