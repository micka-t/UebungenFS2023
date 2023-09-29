import matplotlib.pyplot as plt
import numpy as np
from math import *

x = np.linspace(-np.pi, np.pi, 20)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1, "k-")
plt.plot(x,y2, "b-")
plt.title("Sinus und Cosinus")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.show()                                                               