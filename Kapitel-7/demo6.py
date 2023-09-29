import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from math import *

ax = plt.axes()

kreis = patches.Circle((0,0), radius=1.0, facecolor=(0.5,0.5,0), edgecolor=(1,0,0), linewidth=5)
#Abkürzungen: facecolor = fc, edgecolor = ec, linewidth = lw

ax.add_patch(kreis)
plt.axis("equal")
plt.show()
