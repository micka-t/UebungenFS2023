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

        button = QPushButton("y=x^2x")
        button2 = QPushButton("y=sin(x)")

        layout.addWidget(self.canvas)
        layout.addWidget(button)
        layout.addWidget(button2)

        center = QWidget()
        center.setLayout(layout)

        button.clicked.connect(self.plot)
        button2.clicked.connect(self.plot2)

        self.setCentralWidget(center)
        self.show()



    def plot(self):
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

app = QApplication([])
window = Window()
app.exec()