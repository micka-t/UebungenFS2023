import matplotlib.pyplot as plt
import numpy as np
from math import *

x = np.linspace(-np.pi, np.pi, 20)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(2)
ax[0].plot(x,y1, "k-")
ax[1].plot(x,y2, "b-")
ax[0].grid(True)
ax[1].grid(True)
ax[0].axis("equal")
ax[1].axis("equal")
plt.show()             