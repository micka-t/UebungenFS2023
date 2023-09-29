class Temperatur:
    def __init__(self, c=0):
        self.c = c
    
    def __str__(self):
        return f"{self.c} °C"
    
    def __gt__(self, other):
        return self.c > other.c
    
    def __lt__(self, other):
        return self.c < other.c
    
    def __eq__(self, other):
        return self.c == other.c
    
    def __ne__(self, other):
        return self.c != other.c



t1 = Temperatur(10)
t2 = Temperatur(19)

if t2.c == t1.c:
    print("Nächste Woche ist die Temperatur gleich")
elif t2.c < t1.c:
    print("Nächste Woche ist die Temperatur tiefer")
else:
    print("Nächste Woche ist die Temperatur höher")
