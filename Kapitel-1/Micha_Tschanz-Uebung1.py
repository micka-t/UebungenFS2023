#Aufgabe 1
#Erstellen Sie eine Klasse Vector3, welche einen dreidimensionalen Vektor repräsentiert.
#Über den Konstruktor werden die Komponenten x, y und z definiert. Wird nichts angegeben, so wird ein Null-Vektor erstellt.
#Entwickeln Sie eine Methode len, welche die Länge des Vektors berechnet.
#Mit einer Instanz von Vector3 soll die Klasse getestet werden.

class Vector3:
    #Konstruktor
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def anzeigen(self):
        print(self.x, self.y, self.z)

    def len(self):
        return (((self.x**2)+(self.y**2)+(self.z**2))**0.5)
    
    def control(self):
        if x == None:
            x = 0
        if y == None:
            y = 0
        if z == None:
            z = 0

v1 = Vector3(3,4,5)
d = v1.len()
print(d)


#Erstellen Sie eine Klasse WGS84Coord welche folgende Attribute hat:
#_longitude (=Länge)
#_latitude (=Breite)
#latitude hat den Wertebereich [-90,90] und longitude hat den Bereich [-180,180].

#Anforderungen:
#a) Im Konstruktor der Klasse kann die Länge und Breite übergeben werden. Der Standard-Wert ist 0.
#b) Stellen sie sicher, dass _longitude und _latitude immer im korrekten Wertebereich sind.
#   Verwenden Sie dazu Setter- und Getter-Methoden Falls ein Wert ausserhalb des zulässigen Bereichs gesetzt wird, so wird dieser korrigiert und eine Warnung wird ausgegeben.
#c) Verwenden Sie Property Attribute anstatt Setter- und Getter-Methoden

class WGS84Coord:
    def __init__(self, longitude, latitude):
        self.setLong(longitude)
        self.setLat(latitude)

    def setLat(self, Value = 0):
        if Value < -90:
           self._latitude = (abs(Value) % 90)*-1
           print("Die Eingabe des Breitengrades lag ausserhalb des definierten Bereiches von -90 und 90. Er wurde korrigiert")
        elif Value > 90:
            self._latitude = Value % 90
            print("Die Eingabe des Breitengrades lag ausserhalb des definierten Bereiches von -90 und 90. Er wurde korrigiert")
        else:
            self._latitude = Value
    def setLong(self, Value = 0):
        if Value < -180:
           self._longitude = (abs(Value) % 180)*-1
           print("Die Eingabe des Längengrades lag ausserhalb des definierten Bereiches von -180 und 180. Er wurde korrigiert")
        elif Value > 180:
            self._longitude = Value % 180
            print("Die Eingabe des Längengrades lag ausserhalb des definierten Bereiches von -180 und 180. Er wurde korrigiert")
        else:
            self._longitude = Value

    def getLong(self):
        return self._longitude
    def getLat(self):
        return self._latitude
    
    
    coord1 = property(getLong, setLong)
    coord2 = property(getLat, setLat)

test = WGS84Coord(200, 65)
print(test.coord1, test.coord2)