class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector2(self.x*other.x, self.y*other.y)

    def __truediv__(self, other): # __floordiv__
        return Vector2(self.x / other.x, self.y / other.y)
    
    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))
    
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    def __len__(self):
        return 2
    
    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError
    
def skalarprodukt(a, b):
    return a.x*b.x + a.y*b.y
    

v1 = Vector2(1,2)
v2 = Vector2(3,4)
v4 = Vector2(10,10)

v3 = v1 + v2
v5 = v1 + v2 + v4
print(v3)
print(v5)
print(v1*v2)

v6 = (v1*v2*v3*v4)
v7 = (v3/v2)
print(v7)