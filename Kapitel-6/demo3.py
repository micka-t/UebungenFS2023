import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import *

class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("UebungenFS2023/Kapitel-6/demo.ui", self)
        self.show()

        self.helloButton.clicked.connect(self.buttonclick)

    def buttonclick(self):
        print("Hello World")

app = QApplication([])
win = UIFenster()
app.exec()