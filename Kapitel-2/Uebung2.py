#Implementieren Sie eine Klasse Vector3, welche einen 3D Vektor repräsentiert.
#Dabei sollen Magische Methoden implementiert werden:
#• Konversion zu Zeichenkette
#• Addition
#• Subtraktion
#• komponentenweise Multiplikation (Vector3 * Vector3)
#• Multiplikation mit Skalar
#(float * Vector3) oder (int * Vector3) oder
#(Vector3 * float) oder (Vector3 * int)

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        if isinstance(other, int or float):
            return Vector3(self.x * other, self.y * other, self.z * other)
    def __rmul__(self, other):
        return self.__mul__(other)

    def dot(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)
    
    def cross(self, other):
        return Vector3((self.y * other.z) - (self.z * other.y),
                    (self.z * other.x) - (self.x * other.z),
                    (self.x * other.y) - (self.y * other.x))

    def laenge(self):
        return ((self.x**2 + self.y**2 + self.z**2)**0.5)
    
    def normalize(self):
        return Vector3((self.x) / ((self.x**2 + self.y**2 + self.z**2)**0.5),
                        self.y  / ((self.x**2 + self.y**2 + self.z**2)**0.5),
                        self.z / ((self.x**2 + self.y**2 + self.z**2)**0.5))    

#Test der Funktionen
a = Vector3(3,4,2)
b = Vector3(2,1,0)
print(a)            # Koversion Zeichenkette
c = a + b           # Addition
print(c)
d = a -b            # Subtraktion
print(d)
e = a * b           # Komponentenweise Multiplikation
print(e)
f = a * 3           # Multiplikation mit Skalar
print(f)
g = a.dot(b)        # Skalarprodukt
print(g)
h = a.cross(b)      # Kreuzprodukt
print(h)
i = a.normalize()   #Normalisierung
print(i)
j = a.laenge()      #Länge des Vektors
print(j)