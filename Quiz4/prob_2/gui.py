# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\QT_GUI_CalculateAverage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(265, 303)
        Dialog.setToolTip("")
        self.pushButton_exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_exit.setGeometry(QtCore.QRect(80, 268, 93, 28))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 231, 241))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(4, 40, 81, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pushButton_calculate = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_calculate.setGeometry(QtCore.QRect(15, 204, 201, 28))
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        self.lineEdit_val1 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_val1.setGeometry(QtCore.QRect(110, 40, 101, 22))
        self.lineEdit_val1.setObjectName("lineEdit_val1")
        self.lineEdit_answer = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_answer.setGeometry(QtCore.QRect(140, 170, 81, 22))
        self.lineEdit_answer.setObjectName("lineEdit_answer")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(4, 170, 111, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(4, 70, 81, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_val2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_val2.setGeometry(QtCore.QRect(110, 70, 101, 22))
        self.lineEdit_val2.setObjectName("lineEdit_val2")
        self.lineEdit_val3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_val3.setGeometry(QtCore.QRect(110, 100, 101, 22))
        self.lineEdit_val3.setObjectName("lineEdit_val3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(4, 100, 81, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(4, 130, 81, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_val4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_val4.setGeometry(QtCore.QRect(110, 130, 101, 22))
        self.lineEdit_val4.setObjectName("lineEdit_val4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Average of 4 numbers"))
        self.pushButton_exit.setText(_translate("Dialog", "Exit"))
        self.groupBox.setTitle(_translate("Dialog", "Average Calculator"))
        self.label.setText(_translate("Dialog", "Value 1"))
        self.pushButton_calculate.setText(_translate("Dialog", "Calculate Average"))
        self.lineEdit_val1.setText(_translate("Dialog", "1.5"))
        self.lineEdit_answer.setText(_translate("Dialog", "2.5"))
        self.label_3.setText(_translate("Dialog", "Average Value"))
        self.label_2.setText(_translate("Dialog", "Value 2"))
        self.lineEdit_val2.setText(_translate("Dialog", "2.0"))
        self.lineEdit_val3.setText(_translate("Dialog", "2.5"))
        self.label_4.setText(_translate("Dialog", "Value 3"))
        self.label_5.setText(_translate("Dialog", "Value 4"))
        self.lineEdit_val4.setText(_translate("Dialog", "4.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())