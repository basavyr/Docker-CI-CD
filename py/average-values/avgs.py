import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rd


randomData = rd.choice([1, 2, 3], size=100)

fct = lambda x: 2 * x + 1

mathValues = list(map(fct,randomData))

print(randomData)

print(mathValues)
