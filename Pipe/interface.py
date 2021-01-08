import random
from Pipe.conn import *
from Pipe.Login import *
from Pipe.inputfile import *
from Pipe.face2 import *
from Pipe.Page3 import *
from Pipe.page4 import *
from Pipe.Process import *
from Risk_Result import *

laolao = NewProjectInfo()
a=[[]]
matrix_group_B=[]
#第一界面
class MyWindows(Ui_LoginForm, QMainWindow):
    def __init__(self):
        super(MyWindows, self).__init__()
        self.setupUi(self)
        self.Button_Login.clicked.connect(self.Login)
        self.button_exit.clicked.connect(self.Close)

    def Close(self):
        self.close()
    def Login(self):
        self.inputText_username.setText('123')
        self.Text_password.setText('123')
        R = bool(Login(self.inputText_username.text(), self.Text_password.text()))
        if R:
            a= QtWidgets.QMessageBox.warning(self, "提示", "登录成功",QMessageBox.Yes)
            inputFlieobj.show()
            self.close()
        else:
            QMessageBox.warning(self,"警告","用户名或密码错误!",QMessageBox.Yes)
            self.inputText_username.setFocus()
#信息录入界面
class inputFlie(QtWidgets.QWidget, Ui_input2):
    def __init__(self):
        super(inputFlie, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.nextstepclick)
        self.pushButton.clicked.connect(self.reset)

    def reset(self):
        # self.close()
        # inputFlieobj = inputFlie()
        # time.sleep(1)
        # inputFlieobj.show()
        i = random.randint(0,99999)
        self.lineEdit_No.setText("A102"+str(i))
        self.lineEdit_Name.setText("石家庄运河桥顶管隧道施工工程")
        self.lineEdit_Location.setText("石家庄")
        self.lineEdit_Designer.setText("铁道建设")
        self.comboBox_Designer.currentText()
        self.lineEdit_Constructor.setText("aaa")
        self.comboBox_Constructor.currentText()
        self.lineEdit_Testing.setText("aaa")
        self.comboBox_Testing.currentText()
        self.lineEdit_Supervisor.setText("aaa")
        self.comboBox_Supervisor.currentText()
        self.lineEdit_9.setText("1000")
        self.lineEdit_8.setText("5.6")
        self.lineEdit_13.setText('1')
        self.lineEdit_14.setText('1')
        self.lineEdit_15.setText('1')
        self.lineEdit_11.setText('1')
        self.lineEdit_12.setText('1')
        self.lineEdit_27.setText('1')
        self.lineEdit_24.setText('1')
        self.lineEdit_25.setText('1')
        self.lineEdit_28.setText('1')
        self.lineEdit_29.setText('1')

        self.comboBox.setCurrentIndex(1)
        self.comboBox_11.setCurrentIndex(1)
        self.comboBox_9.setCurrentIndex(1)
        self.comboBox_10.setCurrentIndex(1)

        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(True)

    def nextstepclick(self):
        U01 = self.lineEdit_No.text()
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
        U11 = float(self.lineEdit_8.text())
        U009 = self.comboBox_6.currentText()
        if U009 == "圆形":
            U09 = 0
            c = self.lineEdit_12.text()
            d = float(c)
            print(c)
            e = {'r':d}
            U12 = json.dumps(e)

        else:
            U09 = 1
            a1 = self.lineEdit_10.text()
            b1 = self.lineEdit_11.text()

            d1 = {'a':float(a1), 'b':float(b1)}
            U12 = json.dumps(d1)
        U13 = self.comboBox_7.currentText()
        if not self.checkBox.isChecked():
            U4 = None
        else:
            dict1 = {'无' :0, '水平平行' :1 ,'上下平行':2,'上下斜交(0°~30°)':3,'上下斜交(30°~60°)':4,'上下斜交(60°~90°)':5,'上下正交':6,'斜上平行':7}

            U411 = float(self.lineEdit_13.text())
            U412 = float(self.lineEdit_14.text())
            U41 = np.sqrt(U411 ** 2 + U412 ** 2)
            U42 = dict1[self.comboBox_11.currentText()]
            U43 = self.lineEdit_15.text()
            e4 = {'U41':U41,'U411':U411,'U412':U412,'U42':U42,'U43':float(U43)}
            U4 = json.dumps(e4)
        if not self.checkBox_2.isChecked():
            U5 = None
        else:
            dict2 = {'无' :0, '水平平行' :1 ,'上下平行':2,'上下斜交(0°~30°)':3,'上下斜交(30°~60°)':4,'上下斜交(60°~90°)':5,'上下正交':6,'斜上平行':7}
            dict3 = {'无' :0, '钢管':1 ,'灰口铸铁管':2,'球墨铸铁管':3}

            U511 = float(self.lineEdit_27.text())
            U512 = float(self.lineEdit_24.text())
            U51 = np.sqrt(U511 ** 2 + U512 ** 2)
            U52 = dict2[self.comboBox_9.currentText()]
            U53 = dict3[self.comboBox.currentText()]
            U54 = self.lineEdit_25.text()
            f5 = {'U51':U51,'U52':U52, 'U511':U511, 'U512':U512, 'U54':float(U54), 'U53':U53}
            U5 = json.dumps(f5)
            # print("U5 ",U5)
            # print("U511",json.loads(U5)["U511"])
            #U5 = '{"U511":0,"U512":2.9,"U52":6,"U53":1,"U54":2.0}'  # 既有邻近地下刚性管线情况12
            #U6 = '{"U61":1,"U62":3.7,"U63":6}'  # 既有邻近邻近基础情况13
        if not self.checkBox_3.isChecked():
            U6= None
        else:
            dict = {'无':0,'条形基础': 1, '筏板基础': 2}
            U61 = dict[self.comboBox_10.currentText()]
            U62 = self.lineEdit_28.text()
            U63 = self.lineEdit_29.text()
            d6 = {'U61':U61, 'U62':float(U62), 'U63':int(U63)}
            U6 = json.dumps(d6)
        U7 = None
        print("input",U01, U02, U03, U04, U31, U05, U32, U06, U33, U07, U34, U08, U11, U09, U12, U13, U4, U5, U6, U7)
        InsertInput(U01, U02, U03, U04, U31, U05, U32, U06, U33, U07, U34, U08, U11, U09, U12, U13, U4, U5, U6, U7)

        InputTran = {'U01':U01, 'U02':U02, 'U03':U03, 'U04':U04, 'U31':U31, 'U05':U05, 'U32':U32, 'U06':U06, 'U33':U33, 'U07':U07, 'U34':U34, 'U08':U08, 'U11':U11, 'U09':U09, 'U12':U12, 'U13':U13, 'U4':U4,'U5':U5, 'U6':U6, 'U7':U7}

        laolao.init(InputTran)
        process=laolao


        # process = Process.NewProjectInfo(U01=U01, U02= U02, U03=U03, U04=U04, U31=U31, U05 = U05, U32 = U32, U06=U06, U33=U33, U07= U07, U34= U34,U08=U08, U11=U11, U09=U09, U12=U12, U13 =U13, U4= U4, U5=U5,U6= U6, U7=U7)

        matrix_group_B = [
            [0.33, 0.33, 0.33],
            [0.33, 0.33, 0.33],
            [0.25, 0.25, 0.25, 0.25],
            [0.25, 0.25, 0.25, 0.25],
            [0.33, 0.33, 0.33]
        ]
        a = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
        A = process.calculate_matrix_A(a)
        B = process.calculate_matrix_B(matrix_group_B, A)
        # for i in process.second_risk():
        #     print(i)


        # print(U01,U02,U03,U04,U31,U05,U32,U06,U33,U07,U34,U08,U11,U09,U12,U13,U4,U5,U6,U7)####################
        # print((U01.strip()) + (U02.strip()) + (U03.strip()) + (U04.strip()) + (U05.strip()) + (U06.strip()) + (U07.strip()) + (U08.strip())\
        #         + (U31.strip()) + (U32.strip()) + (U33.strip()) + (U34.strip()) + (U11.strip()) )
        #
        # if len(U01.strip())>0 & len(U02.strip())>0 & len(U03.strip())>0 & len(U04.strip())>0 & len(U05.strip())>0 & len(U06.strip())>0 & len(U07.strip())>0 & len(U08.strip())>0\
        #         & len(U31.strip())>0 & len(U32.strip())>0 & len(U33.strip())>0 & len(U34.strip())>0 & len(U11.strip())>0 :
        #     conn.InsertInput(U01,U02,U03,U04,U31,U05,U32,U06,U33,U07,U34,U08,U11,U09,U12,U13,U4,U5,U6,U7)
        #     InputTran = dict['U01':U01,'U02':U02,'U03':U03,'U04':U04,'U31':U31,'U05':U05,'U32':U32,'U06':U06,'U33':U33,'U07':U07,'U34':U34,'U08':U08,'U11':U11,'U09':U09,'U12':U12,'U13':U13,'U4':U4,'U5':U5,'U6':U6,'U7':U7]
        #     return (InputTran)
        # else:
        #     QtWidgets.QMessageBox.warning(self, "提示", "输入不能为空",QMessageBox.Yes)
        print("1111")
        self.face2Form = face2()
        print("1111")
        self.face2Form.show()
        # self.close()
        self.hide()

#第二界面
class face2(QtWidgets.QWidget, Ui_face2):
    def __init__(self):
        super(face2, self).__init__()
        self.setupUi(self)
        if laolao.CheckU4():
            U4 = 1
        else:
            U4=None
        if laolao.CheckU5():
            U5 = 1
        else:
            U5=None
        if laolao.CheckU6():
            U6 = 1
        else:
            U6=None
        tag=self.JuZhengWeiShu(U4,U5,U6)
        self.Read_data(U4,U5,U6)
        self.f2nextStepBt.clicked.connect(lambda :self.pushButton_2_nextstep(tag))
        #self.pushButton_2.clicked.connect(self.pushButton_2_shijian)
        self.radioButton_2.clicked['bool'].connect(self.f2_matrix2.setEnabled)
        self.radioButton_2.clicked.connect(self.Remove_data)
        self.radioButton.clicked['bool'].connect(self.f2_matrix2.setDisabled)
        self.radioButton.clicked.connect(lambda :self.Read_data(U4,U5,U6))
    def Remove_data(self):
        print("")

    def Read_data(self,U4,U5,U6):
        self.JuZheng(U4,U5,U6)

    def JuZheng(self,U4,U5,U6):
        self.dir_path = sys.path[0] + "\风险评估V2.0\CSV配置文件\一级风险因子两两判别表"
        # print("path ",self.dir_path)
        data = pd.read_csv(open(self.dir_path + "\\" + "R1.csv"))
        # print("data ",data)
        if U4 == None and U5 == None and U6 == None:
            col_12 = data[["U1", "U2", "U3", "U4", "U5", "U6"]]  # 获取两列，要用二维数据
            data_12 = np.array(col_12)
            for i in range(0, 6):
                for j in range(0, 6):
                    if i >2 or j>2:
                        self.f2_matrix2.setItem(i, j, QTableWidgetItem())
                    else:
                        self.f2_matrix2.setItem(i, j, QTableWidgetItem(str(data_12[i][j])))
        if U4 == 1 and U5 == None and U6 == None:
            col_12 = data[["U1", "U2", "U3", "U4", "U5", "U6"]]  # 获取两列，要用二维数据
            data_12 = np.array(col_12)
            for i in range(0, 6):
                for j in range(0, 6):
                    if i >3 or j>3:
                        self.f2_matrix2.setItem(i, j, QTableWidgetItem())
                    else:
                        self.f2_matrix2.setItem(i, j, QTableWidgetItem(str(data_12[i][j])))
        if U4 == 1 and U5 == 1 and U6 == None:
            col_12 = data[["U1", "U2", "U3", "U4", "U5", "U6"]]  # 获取两列，要用二维数据
            data_12 = np.array(col_12)
            for i in range(0, 6):
                for j in range(0, 6):
                    if i == 5 and j <= 5 or j == 5 and i <= 5:
                        self.f2_matrix2.setItem(i, j, QTableWidgetItem())
                    else:
                        self.f2_matrix2.setItem(i, j, QTableWidgetItem(str(data_12[i][j])))
        if U4 == None and U5 == 1 and U6 == None:
            col_12 = data[["U1", "U2", "U3", "U4", "U5", "U6"]]  # 获取两列，要用二维数据
            data_12 = np.array(col_12)
            for i in range(0, 6):
                    for j in range(0, 6):
                        if i== 3  or j== 3 or  i>4 or j>4:
                            self.f2_matrix2.setItem(i, j, QTableWidgetItem())
                        else:
                            self.f2_matrix2.setItem(i, j, QTableWidgetItem(str(data_12[i][j])))
        if U4 == None and U5 == 1 and U6 == 1:
            col_12 = data[["U1", "U2", "U3", "U4", "U5", "U6"]]  # 获取两列，要用二维数据
            data_12 = np.array(col_12)
            for i in range(0, 6):
                    for j in range(0, 6):
                        if i== 3  or j== 3 :
                            self.f2_matrix2.setItem(i, j, QTableWidgetItem())
                        else:
                            self.f2_matrix2.setItem(i, j, QTableWidgetItem(str(data_12[i][j])))
        if U4 == None and U5 == None and U6 == 1:
            col_12 = data[["U1", "U2", "U3", "U4", "U5", "U6"]]  # 获取两列，要用二维数据
            data_12 = np.array(col_12)
            for i in range(0, 6):
                    for j in range(0, 6):
                        if i> 2 and i<=4  or j> 2 and j<= 4 :
                            self.f2_matrix2.setItem(i, j, QTableWidgetItem())
                        else:
                            self.f2_matrix2.setItem(i, j, QTableWidgetItem(str(data_12[i][j])))
        if U4 == 1 and U5 == None and U6 == 1:
            col_12 = data[["U1", "U2", "U3", "U4", "U5", "U6"]]  # 获取两列，要用二维数据
            data_12 = np.array(col_12)
            for i in range(0, 6):
                    for j in range(0, 6):
                        if i== 4  or j== 4 :
                            self.f2_matrix2.setItem(i, j, QTableWidgetItem())
                        else:
                            self.f2_matrix2.setItem(i, j, QTableWidgetItem(str(data_12[i][j])))
        if U4 == 1 and U5 == 1 and U6 == 1:
            col_12 = data[["U1", "U2", "U3", "U4", "U5", "U6"]]  # 获取两列，要用二维数据
            data_12 = np.array(col_12)
            for i in range(0, 6):
                for j in range(0, 6):
                    self.f2_matrix2.setItem(i, j, QTableWidgetItem(str(data_12[i][j])))
    def pushButton_2_nextstep(self,tag):
        #messagebox.showinfo("提示", "我是一个提示框")
        # 判断C.R的值
        '''
        CR = 0.05
        if CR >= 0.1:
            QtWidgets.QMessageBox.warning(self, "数据检查结果", "计算得出C.R > 0.1!\n请修改数据！", QtWidgets.QMessageBox.Yes)
        # 下一步
        if CR < 0.1:
            # 获取界面2矩阵的值
            row, col = 0, 0
            # 界面返回的矩阵是 f2_matrix
            f2_matrix = np.mat(np.random.rand(6, 6))
            while row < 6:
                while col < 6:
                    f2_matrix[row, col] = self.f2_matrix2.item(row, col).text()
                    col += 1
                col = 0
                row += 1
        '''
        # 界面返回的矩阵是 f2_matrix
        row, col ,i,j= 0, 0,0,0
        f2_matrix = np.mat(np.random.rand(tag, tag))
        print("pushButton_2_nextstep")
        print(self.f2_matrix2.item(0, 3).text())
        if self.f2_matrix2.item(0, 3).text()=='':
            print("pushButton_2_nextstep")
        while row < 6:
            if self.f2_matrix2.item(row, col).text() !='':
                while col < 6:
                    #print(self.f2_matrix2.item(row, col).text())
                    if self.f2_matrix2.item(row, col).text() == '':
                        col += 1
                    else:
                        f2_matrix[i, j] = self.f2_matrix2.item(row, col).text()
                        j += 1
                        col += 1
                col = 0
                j = 0
                i += 1
                row += 1
            else:
                row += 1
        print(f2_matrix)
        global a
        a = f2_matrix
        if laolao.calculate_matrix_A(f2_matrix) ==False:
            QtWidgets.QMessageBox.warning(self, "数据检查结果", "计算得出C.R > 0.1!\n请修改数据！", QtWidgets.QMessageBox.Yes)
        else:
            self.Page3Form = Page3()
            self.Page3Form.show()
            # self.close()
            self.hide()

    def JuZhengWeiShu(self,U4,U5,U6):
        if U4 == None and U5 == None and U6 == None:
            tag=3
        if U4 == 1 and U5 == None and U6 == None:
            tag=4
        if U4 == 1 and U5 == 1 and U6 == None:
            tag = 5
        if U4 == None and U5 == 1 and U6 == None:
            tag = 4
        if U4 == None and U5 == 1 and U6 == 1:
            tag = 5
        if U4 == None and U5 == None and U6 == 1:
            tag = 4
        if U4 == 1 and U5 == None and U6 == 1:
            tag = 5
        if U4 == 1 and U5 == 1 and U6 == 1:
            tag = 6
        return tag


#第三界面
class Page3(QtWidgets.QWidget, Ui_Page3):
    signal_2 = pyqtSignal(str)
    def __init__(self):
        super(Page3, self).__init__()
        self.setupUi(self)
        if laolao.CheckU4():
            U4 = 1
        else:
            U4=None
        if laolao.CheckU5():
            U5 = 1
        else:
            U5=None
        if laolao.CheckU6():
            U6 = 1
        else:
            U6=None
        print(U4,U5,U6)
        self.Read_data(U4,U5,U6)
        self.pushButton_page3_return.clicked.connect(self.pushButton_2_back)
        self.pushButton_page3_next.clicked.connect(lambda :self.pushButton_2_nextstep(U4,U5,U6))
        self.radioButton_face3_read.clicked.connect(lambda :self.Read_data(U4,U5,U6))
        self.radioButton_face3_write.clicked.connect(self.Remove_data)

    def pushButton_2_back(self):
        #返回
        print("返回")

    def pushButton_2_nextstep(self,U4,U5,U6):
        #messagebox.showinfo("提示", "我是一个提示框")
        #self.Send_Data()
        CR_Value=self.Send_Data(U4,U5,U6)
        if CR_Value != False:
            self.Page4Form = Page4()
            self.Page4Form.show()
            # self.close()
            self.hide()
        else:
            QtWidgets.QMessageBox.warning(self, "数据检查结果", "计算得出C.R > 0.1!\n请修改数据！", QtWidgets.QMessageBox.Yes)
            global matrix_group_B
            matrix_group_B=[]

    def Read_data(self,U4,U5,U6):
        self.dir_path = sys.path[0] + "\风险评估V2.0\CSV配置文件\二级风险因子两两判别表"
        data = pd.read_csv(open(self.dir_path+"\\"+"R2_U1.csv"))
        R2_U1 = data[["U11", "U12", "U13"]]  # 获取两列，要用二维数据
        data_R2_U1 = np.array(R2_U1)
        for i in range(0, 3):
            for j in range(0, 3):
                self.tableWidget_3_U1.setItem(i, j, QTableWidgetItem(str(data_R2_U1[i][j])))
        data = pd.read_csv(open(self.dir_path + "\\" + "R2_U2.csv"))
        R2_U2 = data[["U21", "U22", "U23"]]  # 获取两列，要用二维数据
        data_R2_U2 = np.array(R2_U2)
        for i in range(0, 3):
            for j in range(0, 3):
                self.tableWidget_3_U2.setItem(i, j, QTableWidgetItem(str(data_R2_U2[i][j])))
        data = pd.read_csv(open(self.dir_path + "\\" + "R2_U3.csv"))
        R2_U3 = data[["U31", "U32", "U33", "U34"]]  # 获取两列，要用二维数据
        data_R2_U3 = np.array(R2_U3)
        for i in range(0, 4):
            for j in range(0, 4):
                self.tableWidget_3_U3.setItem(i, j, QTableWidgetItem(str(data_R2_U3[i][j])))
        if (U4)==1:
            data = pd.read_csv(open(self.dir_path + "\\" + "R2_U4.csv"))
            R2_U4 = data[["U41", "U42", "U43"]]  # 获取两列，要用二维数据
            data_R2_U4 = np.array(R2_U4)
            for i in range(0, 3):
                for j in range(0, 3):
                    self.tableWidget_3_U4.setItem(i, j, QTableWidgetItem(str(data_R2_U4[i][j])))
        else:
            for i in range(0, 3):
                for j in range(0, 3):
                    self.tableWidget_3_U4.setItem(i, j, QTableWidgetItem(None))

        if (U5)==1:
            data = pd.read_csv(open(self.dir_path + "\\" + "R2_U5.csv"))
            R2_U5 = data[["U51", "U52", "U53", "U54"]]  # 获取两列，要用二维数据
            data_R2_U5 = np.array(R2_U5)
            for i in range(0, 4):
                for j in range(0, 4):
                    self.tableWidget_3_U5.setItem(i, j, QTableWidgetItem(str(data_R2_U5[i][j])))
        else:
            for i in range(0, 4):
                for j in range(0, 4):
                    self.tableWidget_3_U5.setItem(i, j, QTableWidgetItem(None))
        if (U6)==1:
            data = pd.read_csv(open(self.dir_path + "\\" + "R2_U6.csv"))
            R2_U6 = data[["U61", "U62", "U63"]]  # 获取两列，要用二维数据
            data_R2_U6 = np.array(R2_U6)
            for i in range(0, 3):
                for j in range(0, 3):
                    self.tableWidget_3_U6.setItem(i, j, QTableWidgetItem(str(data_R2_U6[i][j])))
        else:
            for i in range(0, 3):
                for j in range(0, 3):
                    self.tableWidget_3_U6.setItem(i, j, QTableWidgetItem(None))
    def Remove_data(self):
        print('')
    def Send_Data(self,U4,U5,U6):
        # 获取界面3矩阵的值
        # 获取界面3矩阵的值
        row, col = 0, 0
        f3_matrix1 = np.mat(np.random.rand(3, 3))
        f3_matrix2 = np.mat(np.random.rand(3, 3))
        f3_matrix3 = np.mat(np.random.rand(4, 4))
        f3_matrix4 = np.mat(np.random.rand(3, 3))
        f3_matrix5 = np.mat(np.random.rand(4, 4))
        f3_matrix6 = np.mat(np.random.rand(3, 3))
        while row < 3:
            while col < 3:
                f3_matrix1[row, col] = self.tableWidget_3_U1.item(row, col).text()
                col += 1
            col = 0
            row += 1
        row, col = 0, 0
        while row < 3:
            while col < 3:
                f3_matrix2[row, col] = self.tableWidget_3_U2.item(row, col).text()
                col += 1
            col = 0
            row += 1
        row, col = 0, 0
        while row < 4:
            while col < 4:
                f3_matrix3[row, col] = self.tableWidget_3_U3.item(row, col).text()
                col += 1
            col = 0
            row += 1
        laolao = NewProjectInfo()
        matrix1 = laolao.calculate_matrix_A(f3_matrix1)
        #print(matrix1)
        matrix2 = laolao.calculate_matrix_A(f3_matrix2)
        #print(matrix2)
        matrix3 = laolao.calculate_matrix_A(f3_matrix3)
        #print(matrix3)
        global matrix_group_B
        matrix_group_B.append(matrix1)
        matrix_group_B.append(matrix2)
        #print(matrix_group_B)
        matrix_group_B.append(matrix3)
        print(matrix_group_B)
        if matrix1 ==False or matrix2 ==False or matrix3 ==False:
            return False
        '''
        matrix_group_B=np.vstack([matrix1,matrix2])
        print(matrix_group_B)
        matrix_group_B = np.vstack([matrix_group_B, matrix2])
        print(matrix_group_B)
        '''
        if U4==1:
            row, col = 0, 0
            while row < 3:
                while col < 3:
                    f3_matrix4[row, col] = self.tableWidget_3_U4.item(row, col).text()
                    col += 1
                col = 0
                row += 1
            matrix4 = laolao.calculate_matrix_A(f3_matrix4)
            matrix_group_B.append(matrix4)
            if matrix4 == False :
                return False
            print(matrix_group_B)
        if U5==1:
            row, col = 0, 0
            while row < 4:
                while col < 4:
                    f3_matrix5[row, col] = self.tableWidget_3_U5.item(row, col).text()
                    col += 1
                col = 0
                row += 1
            matrix5 = laolao.calculate_matrix_A(f3_matrix5)
            matrix_group_B.append(matrix5)
            if matrix5 == False :
                return False
            #print(matrix_group_B)
        if U6==1:
            row, col = 0, 0
            while row < 3:
                while col < 3:
                    f3_matrix6[row, col] = self.tableWidget_3_U6.item(row, col).text()
                    col += 1
                col = 0
                row += 1
            matrix6 = laolao.calculate_matrix_A(f3_matrix6)
            matrix_group_B.append(matrix6)
            if matrix6 == False :
                return False
            print(matrix_group_B)
        '''
        prepare_list = locals()
        for i in range(1, 7):
            print("f3_matrix" + str(i) + "=", prepare_list['f3_matrix' + str(i)])
        '''

#第四界面
class Page4(QtWidgets.QWidget, Ui_Page4):
    def __init__(self):
        super(Page4, self).__init__()
        self.setupUi(self)
        print("page 4 U01",laolao.U01)

        U11=laolao.U11
        isRP2_U12=laolao.U09
        if isRP2_U12 == 0:
            U12 = json.loads(laolao.U12)["r"]
        elif isRP2_U12 == 1:
            U12 = json.loads(laolao.U12)["a"]
        U31 = laolao.U31
        U32 = laolao.U32
        U33 = laolao.U33
        U34 = laolao.U34
        if laolao.CheckU4():
            U41 = json.loads(laolao.U4)["U41"]############无此值，计算
            U42 = json.loads(laolao.U4)["U42"]
            U43 = json.loads(laolao.U4)["U43"]
        else:
            U41 = None
            U42 = None
            U43 = None
        if laolao.CheckU5():
            U51 = json.loads(laolao.U5)["U51"]
            U52 = json.loads(laolao.U5)["U52"]
            U53 = json.loads(laolao.U5)["U53"]
            U54 = json.loads(laolao.U5)["U54"]
            print("Page4", U51)
        else:
            U51 = None
            U52 = None
            U53 = None
            U54 = None

        if laolao.CheckU6():
            U61 = json.loads(laolao.U6)["U61"]
            U62 = json.loads(laolao.U6)["U62"]
            U63 = json.loads(laolao.U6)["U63"]
        else:
            U61 = None
            U62 = None
            U63 = None
        # print("page 4 U11", U11,type(U11))
        # print("page 4 U12", isRP2_U12,U12)
        # print("page 4 U3", U31,U32,U33,U34)
        # print("page 4 U4", U41, U42, U43)
        # print("page 4 U5", U51,U52,U53)
        # print("page 4 U61", U61)
        # print("page 4 U62", U62)
        # print("page 4 U63", U63)

        self.display_tableWidget_content(U11,isRP2_U12,U12,U31,U32,U33,U34,U41,U42,U43,U51,U52,U53,U54,U61,U62,U63)
        self.pushButton_page4_next.clicked.connect(self.pushButton_next)
        self.radioButton.clicked.connect(lambda:self.Read(U11,isRP2_U12,U12,U31,U32,U33,U34,U41,U42,U43,U51,U52,U53,U54,U61,U62,U63))
        self.radioButton_2.clicked.connect(self.XiuGai)

    def pushButton_next(self):

        self.Risk_ResultForm = Risk_Result()
        self.Risk_ResultForm.show()
        # self.close()
        self.hide()

    def Read(self,U11,isRP2_U12,U12,U31,U32,U33,U34,U41,U42,U43,U51,U52,U53,U54,U61,U62,U63):
        self.display_tableWidget_content(U11,isRP2_U12,U12,U31,U32,U33,U34,U41,U42,U43,U51,U52,U53,U54,U61,U62,U63)
    def XiuGai(self):
        print("radioButton_2")
    def display_tableWidget_content(self,U11,isRP2_U12,U12,U31,U32,U33,U34,U41,U42,U43,U51,U52,U53,U54,U61,U62,U63):
        self.dir_path = sys.path[0] + "\风险评估V2.0\CSV配置文件\二级风险因子发生概率隶属度表"
        data = pd.read_csv(open(self.dir_path +"\\"+"RP2_U11.csv", encoding='gb2312'))
        data_0 = np.array(data)
        i = 0
        tableWidget_content_Hang = 2
        while data_0[i][1] != None:
            if int(U11) <= int(data_0[i][1]):
                for k in range(3,8):
                    self.tableWidget_content.setItem(tableWidget_content_Hang, k, QTableWidgetItem(str(data_0[i][k-1])))
                    '''
                self.tableWidget_content.setItem(2, 3, QTableWidgetItem(str(data_0[i][2])))
                self.tableWidget_content.setItem(2, 4, QTableWidgetItem(str(data_0[i][3])))
                self.tableWidget_content.setItem(2, 5, QTableWidgetItem(str(data_0[i][4])))
                self.tableWidget_content.setItem(2, 6, QTableWidgetItem(str(data_0[i][5])))
                self.tableWidget_content.setItem(2, 7, QTableWidgetItem(str(data_0[i][6])))
                '''
                break
            else:
                i = i + 1

        tableWidget_content_Hang=tableWidget_content_Hang+1
        data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U12.csv", encoding='gb2312'))
        #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U12.csv", encoding='gb2312')
        i = 0
        if int(isRP2_U12)==0:
            data_U12=np.array(data.loc[1:4])
            while data_U12[i][1] != None:
                #print(float(data_U12[i][1]))
                if U12 <= float(data_U12[i][1]):
                    for k in range(3, 8):
                        self.tableWidget_content.setItem(tableWidget_content_Hang, k,QTableWidgetItem(str(data_U12[i][k])))
                        '''
                    self.tableWidget_content.setItem(3, 3, QTableWidgetItem(str(data_U12[i][3])))
                    self.tableWidget_content.setItem(3, 4, QTableWidgetItem(str(data_U12[i][4])))
                    self.tableWidget_content.setItem(3, 5, QTableWidgetItem(str(data_U12[i][5])))
                    self.tableWidget_content.setItem(3, 6, QTableWidgetItem(str(data_U12[i][6])))
                    self.tableWidget_content.setItem(3, 7, QTableWidgetItem(str(data_U12[i][7])))
                    '''
                    break
                else:
                    i = i + 1
        else:
            data_U12 = np.array(data.loc[5:9])
            while data_U12[i][1] != None:
                #print(float(data_U12[i][1]))
                if U12 <= float(data_U12[i][1]):
                    for k in range(3, 8):
                        self.tableWidget_content.setItem(tableWidget_content_Hang, k,QTableWidgetItem(str(data_U12[i][k])))
                    break
                else:
                    i = i + 1
        tableWidget_content_Hang = tableWidget_content_Hang + 1

        #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U13.csv", encoding='gb2312')
        data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U13.csv", encoding='gb2312'))
        data_U13 = np.array(data.loc[0])
        for k in range(3, 8):
            self.tableWidget_content.setItem(tableWidget_content_Hang, k, QTableWidgetItem(str(data_U13[k-1])))
        tableWidget_content_Hang = tableWidget_content_Hang + 1
        #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U21.csv", encoding='gb2312')
        data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U21.csv", encoding='gb2312'))
        data_U21 = np.array(data.loc[0])
        for k in range(3, 8):
            self.tableWidget_content.setItem(tableWidget_content_Hang, k, QTableWidgetItem(str(data_U21[k - 1])))
        tableWidget_content_Hang = tableWidget_content_Hang + 1
        #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U22.csv", encoding='gb2312')
        data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U22.csv", encoding='gb2312'))
        data_U22 = np.array(data.loc[0])
        for k in range(3, 8):
            self.tableWidget_content.setItem(tableWidget_content_Hang, k, QTableWidgetItem(str(data_U22[k - 1])))
        tableWidget_content_Hang = tableWidget_content_Hang + 1
        #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U23.csv", encoding='gb2312')
        data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U23.csv", encoding='gb2312'))
        data_U23 = np.array(data.loc[0])
        for k in range(3, 8):
            self.tableWidget_content.setItem(tableWidget_content_Hang, k, QTableWidgetItem(str(data_U23[k - 1])))
        tableWidget_content_Hang = tableWidget_content_Hang + 1
        #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U31.csv", encoding='gb2312')
        data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U31.csv", encoding='gb2312'))
        data_U31 = np.array(data)
        i = 0
        while data_U31[i][0] != None:
            if U31== data_U31[i][0]:
                for k in range(3, 8):
                    self.tableWidget_content.setItem(tableWidget_content_Hang, k,QTableWidgetItem(str(data_U31[i][k - 2])))
                break
            else:
                i = i + 1
        tableWidget_content_Hang = tableWidget_content_Hang + 1
        #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U32.csv", encoding='gb2312')
        data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U32.csv", encoding='gb2312'))
        data_U32 = np.array(data)
        i = 0
        while data_U31[i][0] != None:
            if U32 == data_U32[i][0]:
                for k in range(3, 8):
                    self.tableWidget_content.setItem(tableWidget_content_Hang, k,QTableWidgetItem(str(data_U32[i][k - 2])))
                break
            else:
                i = i + 1
        tableWidget_content_Hang = tableWidget_content_Hang + 1
        #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U33.csv", encoding='gb2312')
        data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U33.csv", encoding='gb2312'))
        data_U33 = np.array(data)
        i = 0
        while data_U33[i][0] != None:
            if U33 == data_U33[i][0]:
                for k in range(3, 8):
                    self.tableWidget_content.setItem(tableWidget_content_Hang, k,QTableWidgetItem(str(data_U33[i][k - 2])))
                break
            else:
                i = i + 1
        tableWidget_content_Hang = tableWidget_content_Hang + 1
        #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U34.csv", encoding='gb2312')
        data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U34.csv", encoding='gb2312'))
        data_U34 = np.array(data)
        i = 0
        while data_U34[i][0] != None:
            if U34 == data_U34[i][0]:
                for k in range(3, 8):
                    self.tableWidget_content.setItem(tableWidget_content_Hang, k,QTableWidgetItem(str(data_U34[i][k - 2])))
                break
            else:
                i = i + 1
        tableWidget_content_Hang = tableWidget_content_Hang + 1
        if U41!=None and U42!=None and U43!=None:
            #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U41.csv", encoding='gb2312')
            data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U41.csv", encoding='gb2312'))
            data_U41 = np.array(data)
            i = 0
            while data_U41[i][1] != None:
                if float(U41) <= float(data_U41[i][1]):
                    for k in range(3, 8):
                        self.tableWidget_content.setItem(tableWidget_content_Hang, k,
                                                         QTableWidgetItem(str(data_U41[i][k - 1])))
                    break
                else:
                    i = i + 1
            tableWidget_content_Hang = tableWidget_content_Hang + 1
            #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U42.csv", encoding='gb2312')
            data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U42.csv", encoding='gb2312'))
            data_U42 = np.array(data)
            i = 0
            while data_U42[i][0] != None:
                if float(U42) == float(data_U42[i][0]):
                    for k in range(3, 8):
                        self.tableWidget_content.setItem(tableWidget_content_Hang, k,
                                                         QTableWidgetItem(str(data_U42[i][k - 1])))
                    break
                else:
                    i = i + 1
            tableWidget_content_Hang = tableWidget_content_Hang + 1
            #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U43.csv", encoding='gb2312')
            data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U43.csv", encoding='gb2312'))
            data_U43 = np.array(data)
            i = 0
            while data_U43[i][1] != None:
                if float(U43) <= float(data_U43[i][1]):
                    for k in range(3, 8):
                        self.tableWidget_content.setItem(tableWidget_content_Hang, k,QTableWidgetItem(str(data_U43[i][k - 1])))
                    break
                else:
                    i = i + 1
        else:
            for tableWidget_content_Hang in range (12,15):
                for k in range(3, 8):
                    self.tableWidget_content.setItem(tableWidget_content_Hang, k, QTableWidgetItem())
        tableWidget_content_Hang=15

        if U51!=None and U52!=None and U53!=None and U54!=None:
            #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U51.csv", encoding='gb2312')
            data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U51.csv", encoding='gb2312'))
            data_U51 = np.array(data)
            i = 0
            while data_U51[i][1] != None:
                if float(U51) <= float(data_U51[i][1]):
                    for k in range(3, 8):
                        self.tableWidget_content.setItem(tableWidget_content_Hang, k,QTableWidgetItem(str(data_U51[i][k - 1])))
                    break
                else:
                    i = i + 1
            tableWidget_content_Hang = tableWidget_content_Hang + 1
            #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U52.csv", encoding='gb2312')
            data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U52.csv", encoding='gb2312'))
            data_U52 = np.array(data)
            i = 0
            while data_U52[i][0] != None:
                if float(U52) == float(data_U52[i][0]):

                    for k in range(3, 8):
                        self.tableWidget_content.setItem(tableWidget_content_Hang, k,QTableWidgetItem(str(data_U52[i][k - 1])))
                    break
                else:
                    i = i + 1
            tableWidget_content_Hang = tableWidget_content_Hang + 1
            #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U53.csv", encoding='gb2312')
            data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U53.csv", encoding='gb2312'))
            data_U53 = np.array(data)
            i = 0
            while data_U53[i][1] != None:
                if float(U53) <= float(data_U53[i][1]):
                    for k in range(3, 8):
                        self.tableWidget_content.setItem(tableWidget_content_Hang, k, QTableWidgetItem(str(data_U53[i][k - 1])))
                    break
                else:
                    i = i + 1
            tableWidget_content_Hang = tableWidget_content_Hang + 1
            #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U54.csv", encoding='gb2312')
            data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U54.csv", encoding='gb2312'))
            data_U54 = np.array(data)
            i = 0
            while data_U54[i][0] != None:
                if float(U54) == float(data_U54[i][0]):
                    for k in range(3, 8):
                        self.tableWidget_content.setItem(tableWidget_content_Hang, k, QTableWidgetItem(str(data_U54[i][k - 1])))
                    break
                else:
                    i = i + 1
        else:
            for tableWidget_content_Hang in range (15,19):
                for k in range(3, 8):
                    self.tableWidget_content.setItem(tableWidget_content_Hang, k,QTableWidgetItem())
        tableWidget_content_Hang = 19
        if U61!=None and U62!=None and U63!=None:
            #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U61.csv", encoding='gb2312')
            data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U61.csv", encoding='gb2312'))
            data_U61 = np.array(data)
            i = 0
            while data_U61[i][0] != None:
                if float(U61) == float(data_U61[i][0]):
                    for k in range(3, 8):
                        self.tableWidget_content.setItem(tableWidget_content_Hang, k, QTableWidgetItem(str(data_U61[i][k - 1])))
                    break
                else:
                    i = i + 1
            tableWidget_content_Hang = tableWidget_content_Hang + 1
            #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U62.csv", encoding='gb2312')
            data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U62.csv", encoding='gb2312'))
            data_U62 = np.array(data)
            i = 0
            while data_U62[i][1] != None:
                if float(U62) <= float(data_U62[i][1]):
                    for k in range(3, 8):
                        self.tableWidget_content.setItem(tableWidget_content_Hang, k,QTableWidgetItem(str(data_U62[i][k - 1])))
                    break
                else:
                    i = i + 1
            tableWidget_content_Hang = tableWidget_content_Hang + 1
            #data = pd.read_csv("二级风险因子发生概率隶属度表\RP2_U63.csv", encoding='gb2312')
            data = pd.read_csv(open(self.dir_path + "\\" + "RP2_U63.csv", encoding='gb2312'))
            data_U63 = np.array(data)
            i = 0
            while data_U63[i][1] != None:
                if float(U63) <= float(data_U63[i][1]):
                    for k in range(3, 8):
                        self.tableWidget_content.setItem(tableWidget_content_Hang, k,QTableWidgetItem(str(data_U63[i][k - 1])))
                    break
                else:
                    i = i + 1
        else:
            for tableWidget_content_Hang in range (19,22):
                for k in range(3, 8):
                    self.tableWidget_content.setItem(tableWidget_content_Hang, k, QTableWidgetItem())


#第五界面
class Risk_Result(QtWidgets.QWidget, Ui_Risk_Result):
    def __init__(self):
        super(Risk_Result, self).__init__()
        self.setupUi(self)
        #需要赋值的变量，例如低风险，较低风险等
        Low_Risk = '1'
        Lower_Risk = '1'
        Medium_Risk = '1'
        High_Risk = '1'
        Higher_Risk = '1'
        Weight_text = '1'
        Risk_Lv_text = '1'
        Result='较低风险'
        #self.Read_table_data()
        #用于界面的初始赋值
        self.display_Risk_Result(2,Low_Risk,Lower_Risk,Medium_Risk,High_Risk,Higher_Risk,Result)
        #两个个按钮的事件，退出、重置、
        self.TuiChu_button.clicked.connect(self.close)
        self.ChongZhi_button.clicked.connect(lambda:self.display_Risk_Result(2,Low_Risk,Lower_Risk,Medium_Risk,High_Risk,Higher_Risk,Result))
        #复选框选择触发的事件
        self.Risk_number_comboBox.currentIndexChanged.connect(lambda: self.WrittingNotOfOther(self.Risk_number_comboBox.currentIndex(),Weight_text,Risk_Lv_text))  # 点击下拉列表，触发对应事件
   #复选框选择触发的事件的函数
    def WrittingNotOfOther(self, tag,Weight_text,Risk_Lv_text):
        '''
        a = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
        '''
        print(a)
        A = laolao.calculate_matrix_A(a)
        B = laolao.calculate_matrix_B(matrix_group_B, A)
        print("face5")
        list = laolao.second_risk()
        count=len(list)
        if tag == 0:
            self.Cuoshi_text.setText('点到了第0项 ...')
            self.Risk_Name_Lv2.setText('新建顶管埋深')
            for i in range(count):
                if list[i]['second_risk_id']=='u11':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
        if tag == 1:
            self.Cuoshi_text.setText('点到了第1项 ...')
            self.Risk_Name_Lv2.setText('新建顶管尺寸')
            for i in range(count):
                if list[i]['second_risk_id']=='u12':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
        if tag == 2:
            self.Cuoshi_text.setText('点到了第2项 ...')
            self.Risk_Name_Lv2.setText('新建工程土层性质')
            for i in range(count):
                if list[i]['second_risk_id']=='u13':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
        if tag == 3:
            self.Cuoshi_text.setText('点到了第3项 ...')
            self.Risk_Name_Lv2.setText('土舱压力')
            for i in range(count):
                if list[i]['second_risk_id']=='u21':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
        if tag == 4:
            self.Cuoshi_text.setText('点到了第4项 ...')
            self.Risk_Name_Lv2.setText('注浆压力')
            for i in range(count):
                if list[i]['second_risk_id']=='u22':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
        if tag == 5:
            self.Cuoshi_text.setText('点到了第5项 ...')
            self.Risk_Name_Lv2.setText('开挖速度')
            for i in range(count):
                if list[i]['second_risk_id']=='u23':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
        if tag == 6:
            self.Cuoshi_text.setText('点到了第6项 ...')
            self.Risk_Name_Lv2.setText('施工技术状况')
            for i in range(count):
                if list[i]['second_risk_id']=='u31':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
        if tag == 7:
            self.Cuoshi_text.setText('点到了第7项 ...')
            self.Risk_Name_Lv2.setText('施工质量')
            for i in range(count):
                if list[i]['second_risk_id']=='u32':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
        if tag == 8:
            self.Cuoshi_text.setText('点到了第8项 ...')
            self.Risk_Name_Lv2.setText('检测情况')
            for i in range(count):
                if list[i]['second_risk_id']=='u33':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
        if tag == 9:
            self.Cuoshi_text.setText('点到了第9项 ...')
            self.Risk_Name_Lv2.setText('监理情况')
            for i in range(count):
                if list[i]['second_risk_id']=='u34':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
        if tag == 10:
            self.Cuoshi_text.setText('点到了第10项 ...')
            self.Risk_Name_Lv2.setText('新建顶管与邻近柔性管线净距')
            for i in range(count):
                if list[i]['second_risk_id']=='u41':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
                    break
                if i == count-1:
                    self.Weight_text.setText('')  # 影响权重
                    self.Risk_Lv_text.setText('')  # 风险等级
        if tag == 11:
            self.Cuoshi_text.setText('点到了第11项 ...')
            self.Risk_Name_Lv2.setText('新建顶管与邻近柔性管线空间位置关系')
            for i in range(count):
                if list[i]['second_risk_id']=='u42':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
                    break
                if i == count-1:
                    self.Weight_text.setText('')  # 影响权重
                    self.Risk_Lv_text.setText('')  # 风险等级
        if tag == 12:
            self.Cuoshi_text.setText('点到了第12项 ...')
            self.Risk_Name_Lv2.setText('邻近柔性管线管径')
            for i in range(count):
                if list[i]['second_risk_id']=='u43':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
                    break
                if i == count-1:
                    self.Weight_text.setText('')  # 影响权重
                    self.Risk_Lv_text.setText('')  # 风险等级
        if tag == 13:
            self.Cuoshi_text.setText('点到了第13项 ...')
            self.Risk_Name_Lv2.setText('新建顶管与邻近刚性管线净距')
            for i in range(count):
                if list[i]['second_risk_id']=='u51':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
                    break
                if i == count-1:
                    self.Weight_text.setText('')  # 影响权重
                    self.Risk_Lv_text.setText('')  # 风险等级
        if tag == 14:
            self.Cuoshi_text.setText('点到了第14项 ...')
            self.Risk_Name_Lv2.setText('新建顶管与邻近刚性管线空间位置关系')
            for i in range(count):
                if list[i]['second_risk_id']=='u52':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
                    break
                if i == count-1:
                    self.Weight_text.setText('')  # 影响权重
                    self.Risk_Lv_text.setText('')  # 风险等级
        if tag == 15:
            self.Cuoshi_text.setText('点到了第15项 ...')
            self.Risk_Name_Lv2.setText('邻近刚性管线材质')
            for i in range(count):
                if list[i]['second_risk_id']=='u53':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
                    break
                if i == count-1:
                    self.Weight_text.setText('')  # 影响权重
                    self.Risk_Lv_text.setText('')  # 风险等级
        if tag == 16:
            self.Cuoshi_text.setText('点到了第16项 ...')
            self.Risk_Name_Lv2.setText('邻近刚性管线尺寸')
            for i in range(count):
                if list[i]['second_risk_id']=='u54':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
                    break
                if i == count-1:
                    self.Weight_text.setText('')  # 影响权重
                    self.Risk_Lv_text.setText('')  # 风险等级
        if tag == 17:
            self.Cuoshi_text.setText('点到了第17项 ...')
            self.Risk_Name_Lv2.setText('邻近基础形式')
            for i in range(count):
                if list[i]['second_risk_id']=='u61':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
                    break
                if i == count-1:
                    self.Weight_text.setText('')  # 影响权重
                    self.Risk_Lv_text.setText('')  # 风险等级
        if tag == 18:
            self.Cuoshi_text.setText('点到了第18项 ...')
            self.Risk_Name_Lv2.setText('新建顶管与临近基础水平净距')
            for i in range(count):
                if list[i]['second_risk_id']=='u62':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
                    break
                if i == count-1:
                    self.Weight_text.setText('')  # 影响权重
                    self.Risk_Lv_text.setText('')  # 风险等级
        if tag == 19:
            self.Cuoshi_text.setText('点到了第19项 ...')
            self.Risk_Name_Lv2.setText('临近基础高度')
            for i in range(count):
                if list[i]['second_risk_id']=='u63':
                    self.Weight_text.setText(str(float(list[i]['second_risk_weight'])))  # 影响权重
                    self.Risk_Lv_text.setText(str((list[i]['risk_classification'])))  # 风险等级
                    break
                if i == count-1:
                    self.Weight_text.setText('')  # 影响权重
                    self.Risk_Lv_text.setText('')  # 风险等级
  #重置函数
    def display_Risk_Result(self,count,Low_Risk,Lower_Risk,Medium_Risk,High_Risk,Higher_Risk,Result):
        #self.Low_Risk.setText('5')
        # 不可编辑
        '''
        matrix_group_B = [
            [0.33, 0.33, 0.33],
            [0.33, 0.33, 0.33],
            [0.25, 0.25, 0.25, 0.25],
            [0.25, 0.25, 0.25, 0.25],
            [0.33, 0.33, 0.33],
        ]
        '''
        '''
        a = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
        '''
        print(a)
        print(matrix_group_B)
        A = laolao.calculate_matrix_A(a)
        B = laolao.calculate_matrix_B(matrix_group_B, A)
        print("face5")
        list = laolao.second_risk()
        count=len(list)
        self.tableView.setEditTriggers(QTableView.NoEditTriggers)
        #self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.qlist = ['item1', 'item2', 'item3', 'item4']
        #self.listView.setModel(self.qlist)
        self.model1= QStandardItemModel(0,5)
        #设置tableview的标题
        self.model1.setHorizontalHeaderLabels(['一级风险编号','二级风险编号','二级风险名称','影响权重','风险等级'])
        #向tableview插入一行数值
        for row in range(count):
            self.model1.appendRow([
                QStandardItem(list[row]['first_risk_id']),
                QStandardItem(list[row]['second_risk_id']),
                QStandardItem(list[row]['second_risk_name']),
                QStandardItem(str(float(list[row]['second_risk_weight']))),
                QStandardItem(str((list[row]['risk_classification']))),
            ])
        self.tableView.setModel(self.model1)
        Low_Risk=0
        Lower_Risk = 0
        Medium_Risk = 0
        Higher_Risk = 0
        High_Risk=0
        for i in range(count):
            if list[i]['risk_classification']=='低风险':
                Low_Risk=list[i]['second_risk_weight']+Low_Risk
            if list[i]['risk_classification'] == '较低风险':
                Lower_Risk = list[i]['second_risk_weight'] + Lower_Risk
            if list[i]['risk_classification'] == '中等风险':
                Medium_Risk = list[i]['second_risk_weight'] + Medium_Risk
            if list[i]['risk_classification'] == '高风险':
                Higher_Risk = list[i]['second_risk_weight'] + Higher_Risk
            if list[i]['risk_classification'] == '较高风险':
                High_Risk = list[i]['second_risk_weight'] + High_Risk
        List_Risk=[Low_Risk, Lower_Risk, Medium_Risk, High_Risk, Higher_Risk]
        Result=List_Risk.index(max(List_Risk))
        if Result==0:
            self.Result.setText("低风险")
        if Result == 1:
            self.Result.setText("较低风险")
        if Result==2:
            self.Result.setText("中等风险")
        if Result==3:
            self.Result.setText("较高风险")
        if Result==4:
            self.Result.setText("高风险")
        self.Low_Risk.setText(str(round(float(Low_Risk),2)))
        self.Lower_Risk.setText(str(round(float(Lower_Risk),2)))
        self.Medium_Risk.setText(str(round(float(Medium_Risk),2)))
        self.Higher_Risk.setText(str(round(float(Higher_Risk),2)))
        self.High_Risk.setText(str(round(float(High_Risk),2)))

        #重置设置界面值为空
        '''
        self.Cuoshi_text.setText('')
        self.Risk_Name_Lv2.setText('')
        self.Low_Risk.setText('')
        self.Lower_Risk.setText('')
        self.Medium_Risk.setText('')
        self.High_Risk.setText('')
        self.Higher_Risk.setText('')
        self.Weight_text.setText('')
        self.Risk_Lv_text.setText('')
        '''

    def Read_table_data(self):
        '''
        matrix_group_B = [
            [0.33, 0.33, 0.33],
            [0.33, 0.33, 0.33],
            [0.25, 0.25, 0.25, 0.25],
            [0.25, 0.25, 0.25, 0.25],
            [0.33, 0.33, 0.33],
        ]
        '''
        '''
        a = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
        '''
        print(a)
        print(matrix_group_B)
        laolao = NewProjectInfo()
        A = laolao.calculate_matrix_A(a)
        B = laolao.calculate_matrix_B(matrix_group_B, A)
        list= laolao.second_risk()
        for i in laolao.second_risk():
            print(i)
        print(list[0]['first_risk_id'])


if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    my_windows = MyWindows()
    # 初始化
    #input2Form = input2()
    inputFlieobj = inputFlie()
    my_windows.show()

    # Page3Form=Page3()
    # Page4Form = Page4()
    # Risk_ResultForm = Risk_Result()
    # 将窗口控件显示在屏幕上
    #input2Form.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())