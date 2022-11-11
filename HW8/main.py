from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import gui as qt5
import matplotlib.pyplot as plt
import sys
import pandas as pd
import numpy as np

# INITIALIZING GUI
app = QtWidgets.QApplication(sys.argv)
Window1 = QtWidgets.QDialog()
ui = qt5.Ui_Dialog()
ui.setupUi(Window1)

def browseFiles():
    fname = QFileDialog.getOpenFileName(Window1, 'Select File', 'C:\\Users')[0]
    ui.txtFileName.setText(fname)

def calculate():
    data = pd.read_csv(ui.txtFileName.text(), sep='\t', lineterminator='\n')
    data.rename(columns = {'Y\r':'Y'}, inplace = True)
    
    coeffs = None
    x = data['X'].values
    y = data['Y'].values

    plt.scatter(x,y,color='k')
    plt.title('Relation of X and Y')
    plt.xlabel('X')
    plt.ylabel('Y')

    if ui.rbtnLin.isChecked():
        coeffs = np.polyfit(x,y,1)
        func = np.poly1d(coeffs)
        plt.plot(x, func(x), 'r', label="Linear Fit")
        ui.txtEquation.setText(str(func))
    if ui.rbtnQuad.isChecked():
        coeffs = np.polyfit(x,y,2)
        func = np.poly1d(coeffs)
        plt.plot(x, func(x), 'g', label="Quadratic Fit")
        ui.txtEquation.setText(str(func))
    if ui.rbtnCubic.isChecked():
        coeffs = np.polyfit(x,y,3)
        func = np.poly1d(coeffs)
        plt.plot(x, func(x), 'b', label="Cubic Fit")
        ui.txtEquation.setText(str(func))
    if ui.rbtnAll.isChecked():
        coeffs = np.polyfit(x,y,1)
        func = np.poly1d(coeffs)
        plt.plot(x, func(x), 'r', label="Linear Fit")
        coeffs = np.polyfit(x,y,2)
        func = np.poly1d(coeffs)
        plt.plot(x, func(x), 'g', label="Quadratic Fit")
        coeffs = np.polyfit(x,y,3)
        func = np.poly1d(coeffs)
        plt.plot(x, func(x), 'b', label="Cubic Fit")
    plt.legend()
    plt.show()

def graphOutput():
    pass

if __name__ == "__main__":
    Window1.show()
    ui.btnSelect.clicked.connect(browseFiles)
    ui.btnCalc.clicked.connect(calculate)
    ui.btnExit.clicked.connect(app.exit)
    sys.exit(app.exec_())