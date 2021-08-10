import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rd


randomValues = lambda x, dev: x + rd.choice([1, -1], size=1) * dev


def Plot(data, plot_file):
    x = data[0]
    y = data[1]
    plt.plot(x, y, '-*r', label=r'$f(x)$')
    plt.legend(loc='best')
    plt.savefig(plot_file, bbox_inches='tight', dpi=300)
    plt.close()
