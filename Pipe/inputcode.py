import json
from PyQt5.QtWidgets import QWidget
from Pipe.inputfileold import Ui_Form
from PyQt5 import QtCore,QtGui,QtWidgets
from Pipe.conn import InsertInput

class inputFile(Ui_Form,QWidget):
    def __init__(self):
        super(self).__init__()
        self.setupUi()
        self.pushButton_2.clicked.connect(self.tran)
        self.pushButton_2.clicked.connect(self.nextstepclick)
    def tran(self):
        InsertInput(self.nextstepclick())
    def nextstepclick(self):
        print(self.comboBox_Designer.currentText())
        U01 = self.lineEdit_No.text()
        print(U01)
        U02 = self.lineEdit_Name.text()
        U03 = self.lineEdit_Location.text()
        U04 = self.lineEdit_Designer.text()
        U31 = self.comboBox_Designer.currentText()
        U05 = self.lineEdit_Constructor.text()
        U32 = self.comboBox_Constructor.currentText()
        U06 = self.lineEdit_Testing.text()
        U33 = self.comboBox_Testing.currentText()
        U07 = self.lineEdit_Supervisor.text()
        U34 = self.comboBox_Supervisor.currentText()
        U08 = self.lineEdit_9.text()
        U11 = self.lineEdit_8.text()
        U009 = self.comboBox_6.currentText()
        print(U009)
        if U009 == "圆形":
            U09 = 0
            c = self.lineEdit_12.text()
            e = [{'r': c}]
            U12 = json.dumps(e)
        else:
            U09 = 1
            a = self.lineEdit_10.text()
            b = self.lineEdit_11.text()
            d = [{'a': int(a), 'b': int(b)}]
            U12 = json.dumps(d)
            print(U12)

        U13 = self.comboBox_7.currentText()
        print(U13)
        if not self.checkBox.isChecked():
            U4 = None
        else:
            a4 = self.comboBox_11.currentText()
            b4 = self.lineEdit_13.text()
            c4 = self.lineEdit_15.text()
            d4 = self.lineEdit_14.text()
            e4 = [{'a': a4, 'b': b4, 'c': c4, 'd': d4}]
            U4 = json.dumps(e4)

        if not self.checkBox_3.isChecked():
            U5 = None
        else:
            a5 = self.comboBox_9.currentText()
            print(a5)
            b5 = self.lineEdit_27.text()
            c5 = self.lineEdit_24.text()
            d5 = self.lineEdit_25.text()
            e5 = self.lineEdit_26.text()
            f5 = [{'a': a5, 'b': b5, 'c': c5, 'd': d5, 'e': e5}]
            U5 = json.dumps(f5)
            print(U5)
        if not self.checkBox_2.isChecked():
            U6= None
        else:
            a6 = self.comboBox_10.currentText()
            print(a6)
            b6 = self.lineEdit_28.text()
            c6 = self.lineEdit_29.text()
            d6 = [{'a': a6, 'b': b6, 'c': c6}]
            U6 = json.dumps(d6)
        U7 = None
        print(U01,U02,U03,U04,U31,U05,U32,U06,U33,U07,U34,U08,U11,U09,U12,U13,U4,U5,U6,U7)
        return (U01,U02,U03,U04,U31,U05,U32,U06,U33,U07,U34,U08,U11,U09,U12,U13,U4,U5,U6,U7)
import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = input()
    window.show()
    sys.exit(app.exec())




