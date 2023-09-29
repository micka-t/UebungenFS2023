import shapely
from shapely.geometry import Point, Polygon, MultiPoint
from shapely import wkt
import matplotlib.pyplot as plt


Muttenz = Point([47.5347, 7.6424])
print(Muttenz.wkt)

s = "POINT (47.5347, 7.6424)"

p = wkt.load(s)

file = open("UebungenFS2023/Kapitel-9/schweiz.wkt")
ch = file.read()
file.close

schweiz = wkt.loads(ch)

for geometry in schweiz.geoms:
    x,y = geometry.exterior.xy
    plt.plot(x,y)
    plt.show()