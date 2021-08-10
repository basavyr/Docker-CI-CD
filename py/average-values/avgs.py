import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rd


randomData = rd.choice([1, 2, 3], size=100)

fct = lambda x: 2 * x + 1

mathValues = list(map(fct,randomData))

plt.plot(mathValues,'*k',label=r'$f(x)$')
plt.plot(list(randomData),'-r',label=r'$f1(x)$')
plt.legend(loc='best')
plt.savefig('plot_averages.pdf',bbox_inches='tight',dpi=300)
plt.close()