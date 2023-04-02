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
        return f"Punkt: ({self.x},{self.y})"

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
        return f"Kreis: Mittelpunkt = ({self.mittelpunkt.x},{self.mittelpunkt.y}), Radius = ({self.radius.x},{self.radius.y})"
    
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
    
    def flaeche(self):
        f = abs(((self.b.x-self.a.x)*(self.c.y-self.a.y))-((self.c.x-self.a.x)*(self.b.y-self.a.y)))
        return f/2
    
    def __str__(self):
        return f"Dreieck: A = ({self.a.x},{self.a.y}), B = ({self.b.x},{self.b.y}), C = ({self.c.x},{self.c.y})"  

class Rechteck(Figur):
    def __init__(self, a, c):
        super().__init__("Rechteck")
        self.a = a
        self.c = c

    def umfang(self):
        s1 = abs(self.a.x - self.c.x) 
        s2 = abs(self.a.y - self.c.y)  
        return 2*s1 + 2*s2
    
    def flaeche(self):
        s1 = abs(self.a.x - self.c.x) 
        s2 = abs(self.a.y - self.c.y)  
        return s1*s2
    def __str__(self):
        return f"Rechteck: ({self.a.x},{self.a.y}) - ({self.c.x},{self.c.y})"    

class Polygon(Figur):
    def __init__(self, *p):
        super().__init__("Polygon")
        self.p = p

    def umfang(self):
        u = 0
        for i in range(len(self.p)):
            punkt1 = self.p[i]
            if i == (len(self.p)-1):
                punkt2 = self.p[0]
            else:
                punkt2 = self.p[i+1]
            u = u + (math.sqrt(((punkt2.x-punkt1.x)**2) + ((punkt2.y-punkt1.y)**2)))
        return u 

    def flaeche(self):
        f = 0
        for i in range(len(self.p)):
            punkt1 = (self.p[i])
            if i == (len(self.p)-1):
                punkt2 = (self.p[0])
                punkt3 = (self.p[i-1])
            elif i == 0:
                punkt2 = (self.p[i+1])
                punkt3 = (self.p[(len(self.p)-1)]) 
            else:
                punkt2 = (self.p[i+1])
                punkt3 = (self.p[i-1])
            f = f + ((punkt1.x) * (punkt2.y-punkt3.y))
        return f/2    
    def __str__(self):
        return f"Polygon: Anzahl Punkte = {(len(self.p))}"  





A= Punkt(1,5)
B= Punkt(1,2)
C= Punkt(3,4)
D= Punkt(7,9)
K= Punkt(0,0)
P= Polygon(A,B,C)
F= Dreieck(A,B,C)
print(A)
print(P.umfang())
print(P)
print(F.umfang())
print(F.flaeche())
print(P.flaeche())