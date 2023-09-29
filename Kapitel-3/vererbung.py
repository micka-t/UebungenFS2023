import math

class Figur:
    def __init__(self, name):
        self.name = name
    
    def flaeche(self):
        return 0
    
    def umfang(self):
        return 0
    
    def __str__(self):
        return self.name

class Punkt(Figur):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt ({self.x},{self.y})"

class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def flaeche(self):
        return self.radius**2*math.pi
    def umfang(self):
        return self.radius*2*math.pi
    def __str__(self):
        return f"Kreis Mittelpunkt = {self.mittelpunkt}, Radius = {self.radius}"


M = Punkt(2,3)
k1 = Kreis(M, 10)

print(k1)
print(k1.flaeche())

M.x = 5
print(k1)

k1.mittelpunkt.x = -5
print(M)
print(k1)