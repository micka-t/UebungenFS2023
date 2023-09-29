from PyQt5.QtWidgets import *
from PyQt5.uic import *
import random

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("UebungenFS2023/Semesterpruefung/aufgabe_4.ui", self)

        self.randomButton.clicked.connect(self.weisheit)
        self.closeButton.clicked.connect(self.fertig)
        self.show()

    def weisheit(self):
        #Liste wird nicht korrekt gefüllt mit einer Beispielliste klappt es ohne das öffnen des Files.
        list = []
        file = open("weisheiten.txt", "r",  encoding="utf-8")
        for line in file:
            line = file.strip()
            list.append(line)
        file.close() 
        x = random.choice(list)
        self.label.setText(x)
    
    def fertig(self):
        self.close()


app = QApplication([])
window = Window()
app.exec()