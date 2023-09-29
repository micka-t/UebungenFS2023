import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import *

# Eine Qt-Applikation erstellen:
app = QApplication(sys.argv)

window = loadUi("UebungenFS2023/Kapitel-6/demo.ui") # GUI aus ui-File laden:
window.show() # Fenster anzeigen
# Application-Loop starten
app.exec()
