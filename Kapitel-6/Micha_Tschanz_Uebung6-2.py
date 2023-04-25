import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import urllib.parse

class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("UebungenFS2023/Kapitel-6/showmap.ui", self)
        self.show()

        self.map_pushButton.clicked.connect(self.openmap)

    def openmap(self):
        lf = self.laenge_lineEdit.text()
        ldef = urllib.parse.quote(lf)

        bf = self.breite_lineEdit.text()
        bdef = urllib.parse.quote(bf)


        link = f"https://www.google.ch/maps/place/{ldef},{bdef}"
        QDesktopServices.openUrl(QUrl(link))


app = QApplication([])
win = UIFenster()
app.exec()