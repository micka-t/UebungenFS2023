import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow): 
    
    def __init__(self):      # Konstruktor
        super().__init__()   # Konstruktor Basis-Klasse

        #self.setGeometry(10,10,640,480)
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)

        self.setWindowTitle("GUI Programmierung")  # Fenster-Titel setzen
        self.show()  # Fenster anzeigen/sichtbar machen
        
        layout_top = QFormLayout()
        self.vorname = QLineEdit()
        self.name = QLineEdit()
        self.geburtstag = QDateEdit()
        self.adresse = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()
        self.countries = QComboBox()
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.l_save = QPushButton("Save")

        layout_top.addRow("Vorname:", self.vorname)
        layout_top.addRow("Name:", self.name)
        layout_top.addRow("Geburtsdatum:", self.geburtstag)
        layout_top.addRow("Adresse", self.adresse)
        layout_top.addRow("Postleizahl", self.plz)
        layout_top.addRow("Ort:", self.ort)
        layout_top.addRow("Land:", self.countries)
        layout_top.addRow(self.l_save)

        top = QWidget()
        top.setLayout(layout_top)
        self.setCentralWidget(top)
        self.show()


        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        fm_save = QAction("Save", self)
        fm_quit = QAction("Quit", self)
        fm_quit.triggered.connect(self.do_quit)
        fm_save.triggered.connect(self.do_save)
        filemenu.addAction(fm_save)
        filemenu.addAction(fm_quit)

        self.l_save.clicked.connect(self.do_save)

    def do_save(self):
        file = open("output.txt", "w", encoding = "utf-8")
        file.write (f"{self.vorname.text()}, {self.name.text()}, {self.geburtstag.text()}, {self.adresse.text()}, {self.plz.text()}, {self.ort.text()}, {self.countries.currentText()}")
        file.close()

    def do_quit(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    mainwindow = MyWindow()
    mainwindow.raise_()
    app.exec_()

if __name__ == '__main__':
    main()