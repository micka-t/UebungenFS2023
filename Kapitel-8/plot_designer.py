from PyQt5.QtWidgets import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("UebungenFS2023/Kapitel-8/plot_functions.ui", self)

        figure = plt.figure(figsize=(16,9))
        self.canvas = FigureCanvas(figure)
        self.verticalLayout.removeWidget(self.widget)
        self.verticalLayout.insertWidget(0,self.canvas)

        self.button1.clicked.connect(self.plot1)
        self.button2.clicked.connect(self.plot2)
        self.slider.valueChanged.connect(self.updateslider)
        self.show()
        
    def plot1(self):
        plt.clf() #clf = clear figure
        x = np.linspace(-5,5,20)
        y = x**2
        plt.plot(x,y,"bo-")
        plt.axis("equal")
        self.canvas.draw()

    def plot2(self):
        plt.clf() #clf = clear figure
        x = np.linspace(-2*np.pi,2*np.pi,50)
        y = np.sin(x)
        plt.plot(x,y, "ko-")
        plt.axis("equal")
        self.canvas.draw()

    def updateslider(self, value):
        plt.clf()
        x = np.linspace(-2*np.pi,2*np.pi,50)
        y = np.cos(x+value/80)
        y2 = np.cos(x)
        plt.plot(x,y, 'go-')
        plt.plot(x,y2, 'ro-')
        plt.axis("equal")
        self.canvas.draw()
        
app = QApplication([])
window = Window()
app.exec()