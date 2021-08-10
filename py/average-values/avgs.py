import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rd


randomValues = lambda x, dev, n_times: [
    x + rd.choice([1, -1], size=1)[0] * rd.random() for _ in range(n_times)]


def Plot(data, plot_file):
    x = data[0]
    y = data[1]
    plt.plot(x, y, '-*r', label=r'$f(x)$')
    plt.legend(loc='best')
    plt.savefig(plot_file, bbox_inches='tight', dpi=300)
    plt.close()


p = randomValues(3, 0.2, 30)

Plot([[i for i in range(len(p))],
      p], 'plot_random.pdf')
