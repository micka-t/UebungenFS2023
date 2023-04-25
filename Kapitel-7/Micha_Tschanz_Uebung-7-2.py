import matplotlib.pyplot as plt
import numpy as np
from math import *

#Funktion f(x,y)
def f(x, y):
    return np.exp(-x**2) * np.sin(y)

#Erstellen arrays
x = np.linspace(-4, 4, 200)
y = np.linspace(-4, 4, 200)

#Erstellen 2D-Gitter
X, Y = np.meshgrid(x, y)

#Funktion anwenden
Z = f(X,Y)

#Darstellen
plt.pcolormesh(X, Y, Z)
plt.title('Funktion: f(x,y) = exp(-x^2)*sin(y)')
plt.colorbar(label='f(x,y)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

