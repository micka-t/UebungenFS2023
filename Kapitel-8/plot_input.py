from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        
        figure = plt.figure(figsize=(7,7))
        self.canvas = FigureCanvas(figure)

        self.x = QLineEdit("[1,2,3,4,5]")
        self.y = QLineEdit("[1,4,9,16,25]")

        button = QPushButton("Plot")

        layout.addWidget(self.canvas)
        layout.addWidget(self.x)
        layout.addWidget(self.y)
        layout.addWidget(button)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

        button.clicked.connect(self.plot)


    def plot(self):
        plt.clf() #clf = clear figure
        xx = self.x.text()
        yy = self.y.text()
        try:
            x = eval(xx)
            y = eval(yy)
        except:
            QMessageBox.critical(self, "Fehler", "x und y bitte korrekt eingeben")
            return
        try:
            plt.plot(x,y,"bo-")
            plt.axis("equal")
            self.canvas.draw()
        except:
            QMessageBox.critical(self, "Fehler", "Bite Eingabe überprüfen")
            return


app = QApplication([])
window = Window()
app.exec()