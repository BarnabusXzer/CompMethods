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
    ui.txtDisplay1.setText(f'{args[0]:.2f}')
    ui.txtDisplay2.setText(f'{args[1]:.2f}')
    ui.txtDisplay3.setText(f'{args[2]:.2f}')
    ui.txtDisplay4.setText(f'{args[3]:.2f}')
    ui.txtDisplay5.setText(f'{args[4]:.2f}')
    ui.txtDisplay6.setText(f'{args[5]:.2f}')
    ui.txtDisplay7.setText(f'{args[6]:.2f}')
    ui.txtDisplay8.setText(f'{args[7]:.2f}')

def calc():

    # DEFINING INPUTS 
    pressure_low = float(ui.txtInput1.text())
    pressure_high = float(ui.txtInput2.text())

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
    # STATE #4 IS ALWASYS SUBCOOLED SO WE CANNOT USE state4.calc()
    state4.h = state3.h + (state3.v * (state4.p - state3.p)) # state4.calc() CANNOT CALCULATE VALUES IN THE SUBCOOLED REGION

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