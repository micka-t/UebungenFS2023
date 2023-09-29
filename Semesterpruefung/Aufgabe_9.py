import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
    
class Kreis():
    def __init__(self, x,y, r):
        self.x = x
        self.y = y
        self.r = r
    def flaeche(self):
        return (self.r**2)*math.pi
    def umfang(self):
        return (self.r*2)*math.pi
    def mittelpunkt(self):
        return f"Mittelpunkt = ({self.x},{self.y})"
    def draw(self):
        axes = plt.axes()
        circle = patches.Circle((self.x, self.y), radius=self.r, facecolor=(1,1,0))
        axes.add_patch(circle)
        plt.axis("equal")
        plt.plot()
        plt.show()
    


X = Kreis(3,4,5)
print(X.flaeche())        
print(X.umfang())   
print(X.mittelpunkt())
X.draw()