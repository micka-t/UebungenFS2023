#Objektorientierung

class Person:
    def __init__(self, name = "", alter = 0):
        self.name = name
        self.alter = alter
    def print_info(self):
        print(self.name , self.alter)

test = Person("Micha", 22)

test.print_info()

#Magic Methods
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
v1 = Vector(1,3)
v2 = Vector(2,4)

v3 = v1 + v2
v4 = v1 - v2

print(v3)
print(v4)

#Vererbung und Klassendiagramme
import math
class Shape:
    def __init__(self, name):
        self.name = name
    def calculate_area(self):
        return 0
    def __str__(self):
        return self.name
    
class Point(Shape):
    def __init__(self, x, y):
        super().__init__("Point")
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
class Rectangle(Shape):
    def __init__(self, a, c):
        super().__init__("Rectangle")
        self.a = a
        self.c = c
    def calculate_area(self):
        s1 = self.c.x - self.a.x
        s2 = self.c.y - self.a.y
        return s1*s2
    def __str__(self):
        return f"Rechteck: ({self.a.x},{self.a.y}) - ({self.c.x},{self.c.y})"
    
class Circle(Shape):
    def __init__(self, m, r):
        super().__init__("Circle")
        self.m = m
        self.r = r
    def calculate_area(self):
        return (self.r**2)*math.pi
    def __str__(self):
        return f"Kreis: Mittelpunkt = ({self.m.x},{self.m.y}), Radius = {self.r}"
    
A = Point(1,3)
B = Point(3,6)
R1 = Rectangle(A,B)
C1 = Circle(A,3)
print(R1)
print(R1.calculate_area())
print(C1)
print(C1.calculate_area())           

from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5 import QtWidgets

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("UebungenFS2023/Pruefungsvorbereitung/gui1.ui", self)
        self.finish_button.clicked.connect(self.Ausgabe)
        self.open_button.clicked.connect(self.Open)
        self.show()
    def Ausgabe(self):
        self.text = self.texteingabe.text()
        QMessageBox.about(self, "Texteingabe", self.text)

        #Mit findchild (aufwendiger)
        #self.text = self.findChild(QtWidgets.QLineEdit, "texteingabe")
        #self.text_value = self.text.text()
        #QMessageBox.about(self, "Texteingabe", self.text_value)

    def Open(self):

        QFileDialog.getOpenFileNames(self, "Dateien öffnen", "", "Images (*.jpg *.png)")


app = QApplication([])
window = Window()
app.exec()