import gui
from PyQt5 import QtWidgets
import sys  

# INITIALIZING GUI
app = QtWidgets.QApplication(sys.argv)
Window1 = QtWidgets.QDialog()
ui = gui.Ui_Dialog()
ui.setupUi(Window1)

def calc():

    # DEFINING INPUTS
    value1 = float(ui.lineEdit_val1.text())
    value2 = float(ui.lineEdit_val2.text())
    value3 = float(ui.lineEdit_val3.text())
    value4 = float(ui.lineEdit_val4.text())

    average = (value1 + value2 + value3 + value4) / 4
    ui.lineEdit_answer.setText(f'{average:.2f}')

if __name__ == "__main__":
    Window1.show()
    ui.pushButton_calculate.clicked.connect(calc)
    ui.pushButton_exit.clicked.connect(app.exit)
    sys.exit(app.exec_())