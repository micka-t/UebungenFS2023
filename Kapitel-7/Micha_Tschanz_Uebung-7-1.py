import matplotlib.pyplot as plt
import numpy as np
from math import *

x = np.random.random(1000)
x = x*200-100
y = np.random.random(1000)
y = y*200-100
colors = np.random.random(1000)
plt.scatter(x,y, c=colors)
plt.show()
