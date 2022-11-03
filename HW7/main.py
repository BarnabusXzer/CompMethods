import IdealRankineCycleUI as qt5
from SteamState import SteamState
from PyQt5 import QtWidgets
import sys  

# INITIALIZING GUI
app = QtWidgets.QApplication(sys.argv)
Window1 = QtWidgets.QDialog()
ui = qt5.Ui_Window1()
ui.setupUi(Window1)

def setOutput(args):
    ui.txtDisplay1.setText(str(args[0]))
    ui.txtDisplay2.setText(str(args[1]))
    ui.txtDisplay3.setText(str(args[2]))
    ui.txtDisplay4.setText(str(args[3]))
    ui.txtDisplay5.setText(str(args[4]))
    ui.txtDisplay6.setText(str(args[5]))
    ui.txtDisplay7.setText(str(args[6]))
    ui.txtDisplay8.setText(str(args[7]))

def calc():

    # DEFINING INPUTS 
    pressure_high = float(ui.txtInput1.text())
    pressure_low = float(ui.txtInput2.text())
    temp_high_bool = False
    temp_high = None

    if ui.rBtn1.isChecked() == True:
        temp_high_bool = False
    else:
        temp_high_bool = True
        temp_high = float(ui.txtInput3.text())

    # CALCULATE PROPERTIES FOR STATE #1
    state1 = SteamState(pressure_high, 'Turbine Inlet')
    if temp_high_bool == True:
        state1.T = temp_high
    else:
        state1.x = 1.0
    state1.calc()
    
    # CALCULATE PROPERTIES FOR STATE #2
    state2 = SteamState(pressure_low, 'Turbine Exit')
    state2.s = state1.s
    state2.calc()

    # CALCULATE PROPERTIES FOR STATE #3
    state3 = SteamState(pressure_low, 'Pump Entrance')
    state3.x = 0.0
    state3.calc()

    # CALCULATE PROPERTIES FOR STATE #4
    state4 = SteamState(pressure_high, 'Pump Exit')
    state4.x = 0.0
    state4.calc()

    # CALCULATE OUTPUTE VALUES
    turbine_work = state1.h - state2.h
    pump_work = state4.h - state3.h
    heat_added = state1.h - state4.h
    thermal_efficency = (turbine_work - pump_work) / heat_added * 100
    
    output = [state1.h, state2.h, state3.h, state4.h, turbine_work, pump_work, heat_added, thermal_efficency]
    setOutput(output)

if __name__ == "__main__":
    Window1.show()
    ui.btnCalc.clicked.connect(calc)
    ui.btnExit.clicked.connect(app.exit)
    sys.exit(app.exec_())