#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy.random as rd
import numpy as np
import time
import os
import platform
from datetime import datetime

now = lambda: str(datetime.utcnow())[
    0:10] + '-' + str(datetime.utcnow())[11:19]  # get current time

fig = './plots/dockerized_plot'


class Functions:
    def function1(self, arg):
        return arg * arg + 1

    def function2(self, arg, a):
        return a * arg * arg + 1

    def function3(self, arg, a):
        with np.errstate(divide='ignore'):
            x = a * np.log(arg) + np.sin(arg)
        return x


def make_plot(x1, a1, a2):
    print('Starts the plotting procedure')
    # print(f'a1 -> {a1}')
    # print(f'a2 -> {a2}')

    plt.plot(x1, list(map(Functions().function1, x1)), '-or', label='f1')
    plt.plot(x1, list(map(Functions().function2, x1,
                          [a1 for x in x1])), '-og', label='f2')
    plt.plot(x1, list(map(Functions().function3, x1,
                          [a2 for x in x1])), '-ob', label='f3')
    plt.legend(loc='best')

    fig_name = fig + '-' + now() + '.pdf'
    plt.savefig(fig_name, bbox_inches='tight', dpi=300)
    print('Finishing the plotting procedure')
    time.sleep(1)
    plt.close()
    print(f'Plot saved at -> {fig}')


give_a = lambda: rd.choice([1, 2, 3, 4, 5])
x1 = np.arange(0, 3, 0.1)

n_iterations = 5

# for _ in range(n_iterations):
#     make_plot(x1, give_a(), give_a())
machine=platform.uname().version
print(machine.split(' '))