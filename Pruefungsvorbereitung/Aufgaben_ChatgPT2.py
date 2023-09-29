from PyQt5.QtWidgets import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("UebungenFS2023/Pruefungsvorbereitung/gui2.ui", self)

        figure = plt.figure(figsize=(16,9))
        self.canvas = FigureCanvas(figure)
        self.verticalLayout.removeWidget(self.widget)
        self.verticalLayout.insertWidget(0,self.canvas)

        self.randomButton.clicked.connect(self.plot)
        self.show()
        
    def plot(self):
        plt.clf() #clf = clear figure
        x = np.linspace(-5,5,100)
        y = np.sin(x)
        plt.plot(x,y,"b-")
        plt.axis("equal")
        self.canvas.draw()
        
app = QApplication([])
window = Window()
app.exec()