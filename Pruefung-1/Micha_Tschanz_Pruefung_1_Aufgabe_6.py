import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()

    def createLayout(self):
        self.setWindowTitle("Währungsumrechner")

        layout=QFormLayout()
        self.rechnen=QPushButton("Umrechnen")
        self.Franken=QLineEdit()
        self.Euro=QLabel()

        layout.addRow("Schweizer Franken",self.Franken)
        layout.addRow("Euro:",self.Euro)
        layout.addRow(self.rechnen)


    

        center= QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()
    def createConnects(self):
        self.rechnen.clicked.connect(self.rechner)

    def rechner (self):
        self.Euro.setText(str((int((self.Franken.text()))/100)*87.60))

def main():
    app = QApplication(sys.argv)
    mainwindow = MyWindow()
    mainwindow.raise_()
    app.exec_()

if __name__ == '__main__':
    main()