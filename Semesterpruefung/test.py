import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
axes = plt.axes()
circle = patches.Circle((0, 0), radius=1.0, facecolor=(1,1,0))
axes.add_patch(circle)
plt.axis("equal")
plt.plot()
