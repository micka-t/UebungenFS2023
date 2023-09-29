import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow): 
    
    def __init__(self):
        super().__init__()


        self.setMinimumWidth(600)
        self.setMinimumHeight(600)

        self.setWindowTitle("Fenster")
        self.show()
        
        layout_top = QVBoxLayout()
        layout_bottom = QHBoxLayout()
        self.kalender = QCalendarWidget()
        self.titel = QLabel("Ist dieses Datum in Ordnung?")
        self.ja = QPushButton("Ja")
        self.nein = QPushButton("Nein")
        self.abbrechen = QPushButton("Abbrechen")


        layout_top.addWidget(self.kalender)
        layout_top.addWidget(self.titel)
        layout_bottom.addWidget(self.ja)
        layout_bottom.addWidget(self.nein)
        layout_bottom.addWidget(self.abbrechen)
        layout_top.addLayout(layout_bottom)



        top = QWidget()
        top.setLayout(layout_top)
        self.setCentralWidget(top)
        self.show()

def main():
    app = QApplication(sys.argv)
    mainwindow = MyWindow()
    mainwindow.raise_()
    app.exec_()

if __name__ == '__main__':
    main()