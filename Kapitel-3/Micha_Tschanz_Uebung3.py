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
    
class Dreieck(Figur):
    def __init__(self, a, b, c):
        super().__init__("Dreieck")
        self.a = a
        self.b = b
        self.c = c

    def umfang(self):
        ab = math.sqrt((self.b.x - self.a.x)**2 + (self.b.y-self.a.y)**2)    
        bc = math.sqrt((self.c.x - self.b.x)**2 + (self.c.y-self.b.y)**2)    
        ca = math.sqrt((self.a.x - self.c.x)**2 + (self.a.y-self.c.y)**2)    
        return ab + bc + ca
    def __str__(self):
        return f"Eckpunkte: A = {self.a}, B = {self.b}, C = {self.c}"
    


A= Punkt(2,5)
B= Punkt(1,2)
C= Punkt(3,4)
D= Dreieck(A,B,C)
print(D.umfang())
print(D)