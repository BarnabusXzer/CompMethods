from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import gui

# INITIALIZING GUI
app = QtWidgets.QApplication(sys.argv)
Window1 = QtWidgets.QDialog()
ui = gui.Ui_Dialog()
ui.setupUi(Window1)
plot = gui.PlotCanvas(ui.graphicsView)

def browseFiles():
    fname = QFileDialog.getOpenFileName(Window1, 'Select File', 'C:\\Users')[0]
    ui.txtFileName.setText(fname)

def calculate():
    data = pd.read_csv(ui.txtFileName.text(), sep='\t', lineterminator='\n')
    data.rename(columns = {'Y\r':'Y'}, inplace = True)
    
    coeffs = None
    x = data['X'].values
    y = data['Y'].values

    if ui.rbtnLin.isChecked():

        coeffs = np.polyfit(x,y,1)
        func = np.poly1d(coeffs)

        plot.figure.clf()
        ax = plot.figure.add_subplot(111)
        ax.scatter(x,y)
        ax.set_title('Linear Fit')
        ax.plot(x, func(x), 'r')
        ax.axes.set_ylabel('Y Label')
        ax.axes.set_xlabel('X Label')
        plot.draw()

        ui.txtEquation.setText(f'{coeffs[0]:.2f}x + {coeffs[1]:.2f}')

    elif ui.rbtnQuad.isChecked():

        coeffs = np.polyfit(x,y,2)
        func = np.poly1d(coeffs)

        plot.figure.clf()
        ax = plot.figure.add_subplot(111)
        ax.scatter(x,y)
        ax.set_title('Quadratic Fit')
        ax.plot(x, func(x), 'g')
        ax.axes.set_ylabel('Y Label')
        ax.axes.set_xlabel('X Label')
        plot.draw()

        ui.txtEquation.setText(f'{coeffs[0]:.2f}x^2 + {coeffs[1]:.2f}x + {coeffs[2]:.2f}')

    elif ui.rbtnCubic.isChecked():

        coeffs = np.polyfit(x,y,3)
        func = np.poly1d(coeffs)

        plot.figure.clf()
        ax = plot.figure.add_subplot(111)
        ax.scatter(x,y)
        ax.set_title('Cubic Fit')
        ax.plot(x, func(x), 'k')
        ax.axes.set_ylabel('Y Label')
        ax.axes.set_xlabel('X Label')
        plot.draw()

        ui.txtEquation.setText(f'{coeffs[0]:.2f}x^3 + {coeffs[1]:.2f}x^2 + {coeffs[2]:.2f}x + {coeffs[3]:.2f}')

    elif ui.rbtnExp.isChecked():
        def exponential(args):
            A, B, C = args
            response = A + B * np.e ** (C * x)
            return response

        print(minimize(exponential, [x,1,1,1]))    
        # ui.txtEquation.setText(str(func))

    elif ui.rbtnAll.isChecked():

        coeffs = np.polyfit(x,y,1)
        func = np.poly1d(coeffs)
        plt.plot(x, func(x), 'r', label="Linear Fit")

        coeffs = np.polyfit(x,y,2)
        func = np.poly1d(coeffs)
        plt.plot(x, func(x), 'g', label="Quadratic Fit")

        coeffs = np.polyfit(x,y,3)
        func = np.poly1d(coeffs)
        plt.plot(x, func(x), 'b', label="Cubic Fit")

        coeffs = np.polyfit(x,y,3)
        func = np.poly1d(coeffs)
        plt.plot(x, func(x), 'y', label="Exponential Fit")

if __name__ == "__main__":
    Window1.show()
    ui.btnSelect.clicked.connect(browseFiles)
    ui.btnCalc.clicked.connect(calculate)
    ui.btnExit.clicked.connect(app.exit)
    sys.exit(app.exec_())