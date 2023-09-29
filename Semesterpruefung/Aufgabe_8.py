import matplotlib.pyplot as plt
import numpy as np
from math import *

verkaufszahlen = [1500, 1800, 2000, 2200, 2100, 1900, 2300, 2400, 2500, 2800, 2700, 2900]
Monate = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

plt.plot(Monate, verkaufszahlen)
plt.title('Verkaufszahlen pro Monat')
plt.xlabel('Monat')
plt.show()