# print("Hello World")

# punktnummer = 1
# x = 2600000
# y = 1200000
# h = 540.15

# print(punktnummer, x, y, h)                 #nicht schlau!

# punkt1 = [1, 2600000, 1200000, 540.15]
# punkt2 = [2, 0, 0, 0]                       #auch nicht besser!

from punkt import *

p1 = Punkt(1, 2600000, 1200000, 540.15)
p2 = Punkt(2, 0, 0, 0)

#print(p1.x, p1.y, p1.h)
#print(p2.x, p2.y, p2.h)

p1.anzeigen()
p2.anzeigen()

hd = p1.hdiff(p2)
print(hd)

d1 = p1.dist(p2)
d2 = p2.dist(p1)
print(d1, d2)

p1.x = 50
p1.anzeigen()