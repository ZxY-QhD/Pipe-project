import csv
import json
import math
import os
import sys
from math import sqrt

import numpy as np


# U01 = "A101"  # 工程编号
# U02 = "石家庄运河桥顶管隧道施工工程"  # 工程名称
# U03 = "石家庄"  # 工程所在地
# U04 = "铁道建设"  # 设计方
# U05 = "铁道建设"  # 施工方
# U06 = "铁道建设"  # 检测方
# U07 = "铁道建设"  # 监理方
# U08 = "2300"  # 隧道长度
#
# U09 = 0  # 开挖顶管断面形式
#
# U31 = "丙级"  # 设计方资质等级
# U32 = "特级"  # 施工方资质等级
# U33 = "甲级"  # 检测方资质等级
# U34 = "甲级"  # 监理方资质等级
#
# U11 = "5.6"  # 新建顶管埋深
# U12 = '{"r":4.8}'  # 新建顶管尺寸 '{"a":3.0,"b":2.4}'
# U13 = "软黏土"  # 新建工程土层性质
#
# # U4 = '{"U41":2,"U42":3,"U43":5}'#既有邻近地下柔性管线情况11
# U4 = ''
#
# U5 = '{"U511":0,"U512":2.9,"U52":6,"U53":1,"U54":2.0}'  # 既有邻近地下刚性管线情况12
# U6 = '{"U61":1,"U62":3.7,"U63":6}'  # 既有邻近邻近基础情况13
# U7 = ""  # 特殊工程情况说明


# z
DATE = "2020-11-21"
# 以下为没有提供的参数
U21 = 21  # 土舱压力
U22 = 2
U23 = 2

class File_Processing:
    """
     lao = File_Processing()
    # re = lao.read_table_full(r"C:\\Users\坂田银时\Desktop\风险评估软件需求分析与数据库设计相关文档V2.0\V2.0\CSV配置文件\风险等级指标判别表\RLV.csv")
    re = lao.read_table_nofirst_line_nofirst_column(r"C:\\Users\坂田银时\Desktop\风险评估软件需求分析与数据库设计相关文档V2.0\V2.0\CSV配置文件\二级风险因子两两判别表\R2_U1.CSV")
    print(re)
    """

    def read_file(self, file):
        """
        读文件,文件空返回0
        :param file: txt or csv文件
        :return: 文件内容
        """
        # print(file.split("."))
        l = file.split(".")
        index = l[-1]
        file_name = ""
        for i in range(len(l) - 1):
            file_name += l[i]
        # print(file_name,index)
        re = []
        if index == "txt":
            with open(file, "r") as f:
                while True:
                    t = f.readline()
                    if t == "":
                        break
                    re.append(t[:-2])
        if index.upper() == "CSV":
            # print(file)
            with open(file, "r", encoding="gb18030") as f:
                t = csv.reader(f)
                # print(t)
                # 建立空字典
                for item in t:
                    # 忽略第一行
                    # if t.line_num == 1:
                    #     continue
                    re.append(item)
        if len(re) == 0:
            return False, False
        else:
            return file_name, re

    def is_number(self, s):
        try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
            float(s)
            return True
        except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
            pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
        try:
            import unicodedata  # 处理ASCii码的包

            unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
            return True
        except (TypeError, ValueError):
            pass
        return False

    def read_table_full(self, file):
        """
        读取csv文件全部
        :param file: 文件名
        :return: 列表
        """
        file_name, re = self.read_file(file)
        # print(file_name,re)
        if file_name == False:
            return False

        first_risk = []
        for i in re:
            # print(i)
            k = []
            for j in i:
                if self.is_number(j):
                    k.append(eval(j))
                else:
                    k.append(j)
            first_risk.append(k)
        return first_risk

    def read_table_nofirst_line_nofirst_column(self, file):
        """
        读取csv文件
            # Example:

        :param file: 文件名
        :return: 列表
        """
        file_name, re = self.read_file(file)
        # print(file_name,re)
        if file_name == False:
            return False

        first_risk = []
        for i in re[1:]:
            # print(i)
            k = []
            for j in i[1:]:
                if self.is_number(j):
                    k.append(eval(j))
                else:
                    k.append(j)
            first_risk.append(k)
        return first_risk


class NewProjectInfo:
    """
    新建工程信息表
    """


    def init(
        self,
        dict
        #date=DATE,
    ):
        """
        前端控件读取的输入输入这里进行修改
        """
        #self.date = date
        try:
            # self.U01 = dict["a"]
            self.U01 = dict["U01"]
            self.U02 = dict["U02"]
            self.U03 = dict["U03"]
            self.U04 = dict["U04"]
            self.U05 = dict["U05"]
            self.U06 = dict["U06"]
            self.U07 = dict["U07"]
            self.U08 = dict["U08"]
            self.U09 = dict["U09"]
            self.U11 = dict["U11"]
            self.U12 = dict["U12"]
            self.U13 = dict["U13"]
            self.U21 = 1
            self.U22 = 1
            self.U23 = 1
            self.U31 = dict["U31"]
            self.U32 = dict["U32"]
            self.U33 = dict["U33"]
            self.U34 = dict["U34"]
            self.U4 = dict["U4"]
            self.U5 = dict["U5"]
            self.U6 = dict["U6"]
            self.U7 = dict["U7"]
        except Exception as e:
            print(e)

        self.dir_path = sys.path[0] + "\风险评估V2.0\CSV配置文件\二级风险因子发生概率隶属度表"
        self.lao = File_Processing()
        self.pointer_table = [
            [0, 0.2, 0.1, "低风险"],
            [0.2, 0.4, 0.3, "较低风险"],
            [0.4, 0.6, 0.5, "中等风险"],
            [0.6, 0.8, 0.7, "较高风险"],
            [0.8, 1, 0.9, "高风险"],
        ]
        self.matrix_B = [
            ["None", "None", "None", "None"],
            ["None", "None", "None", "None"],
            ["None", "None", "None", "None"],
            ["None", "None", "None", "None"],
            ["None", "None", "None", "None"],
            ["None", "None", "None", "None"],
        ]
        self.second_risk_name = {
            "u11": "新建顶管埋深",
            "u12": "新建顶管尺寸",
            "u13": "新建工程土层性质",
            "u21": "土舱压力",
            "u22": "注浆压力",
            "u23": "开挖速度",
            "u31": "施工技术情况",
            "u32": "施工质量",
            "u33": "检测情况",
            "u34": "监理情况",
            "u41": "新建顶管与邻近柔性管线净距",
            "u42": "新建顶管与邻近柔性管线空间位置关系",
            "u43": "邻近柔性管线管径",
            "u51": "新建顶管与邻近刚性管线净距",
            "u52": "新建顶管与邻近刚性管线空间位置关系",
            "u53": "邻近刚性管线材质",
            "u54": "邻近刚性管线尺寸",
            "u61": "邻近基础形式",
            "u62": "新建顶管与临近基础水平净距",
            "u63": "临近基础高度",
        }

    def calculate_matrix_A(self, matrix):
        """
        计算该矩阵M的特征值λ_max和特征向量A
        最大特征值对应的特征向量A，并进行归一化
        Example:
         lao = NewProjectInfo()
          a = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
        b = lao.CalculateMatrix(a)
        print(b)
        :param matrix:第一行代表列
        :return:C.R<0.1 调用返回答案,C.R>=0.1调用返回false
        """
        print("cal a ")
        RI = {1: 0, 2: 0, 3: 0.52, 4: 0.89, 5: 1.12, 6: 1.24, 7: 1.36, 8: 1.41, 9: 1.46}
        m = np.array(matrix)
        eigenvalue, featurevector = np.linalg.eig(m)
        r_max = 0
        A_id = 0
        for i in range(len(eigenvalue)):
            if r_max < eigenvalue[i]:
                r_max = eigenvalue[i]
                A_id = i
        n = len(matrix)
        A = []
        # print(r_max)
        # print(eigenvalue)
        for i in featurevector:
            A.append(i[A_id])
        # print(A)
        CR = (r_max - n) * RI[n] / (n - 1)
        if CR < 0.1:
            # 归一化
            x = 0
            for i in A:
                x += i
            A_uniformization = []
            for i in A:
                A_uniformization.append(i / x)
            return A_uniformization
        else:
            return False

    def calculate_matrix_B(self, matrix_group_B, A_uniformization):
        """
        Example:
         lao = NewProjectInfo()
         matrix_group_B = [
            [0.33,0.33,0.33],
            [0.33,0.33,0.33],
            [0.25,0.25,0.25,0.25],
            [0.25, 0.25, 0.25, 0.25],
            [0.33,0.33,0.33]
        ]
        a = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
        A = lao.calculate_matrix_A(a)
        B = lao.calculate_matrix_B(matrix_group_B,A)
        for i in B:
        print(i)
        :param matrix_group_B: 5组特征向量
        :param A_uniformization: calculate_matrix_A计算出来的权重
        :return:风险权重
        """
        print("cal b")
        Risk_B = []
        index_a = 0
        for Bi in matrix_group_B:
            t = []
            for i in Bi:
                t.append(round(i * A_uniformization[index_a],3))
            index_a += 1
            Risk_B.append(t)
        self.matrix_B = Risk_B
        print("cbfinsh")
        return Risk_B

    def calculate_waverage_of_risk(self, pointer_table, target_index):
        """
          计算各个风险指标的加权平均值
           输出概率值和风险类型
        Example:
            lao = NewProjectInfo()
            pointer_table = [
                [ 0, 0.2, 0.1, "低风险"],
                [ 0.2, 0.4, 0.3, "较低风险"],
                [ 0.4, 0.6, 0.5, "中等风险"],
                [ 0.6, 0.8, 0.7, "较高风险"],
                [ 0.8, 1, 0.9, "高风险"]
            ]
            target_index = [
                ['低风险','较低风险','中等风险','较高风险','高风险'],
                [ 6, 2, 1, 1, 0]
            ]
            risk_value, risk_classification = lao.calculate_waverage_of_risk(pointer_table, target_index)
            print("风险分类={}".format(risk_classification))
            print("风险值={}".format(risk_value))
        :param pointer_table: 对照表
        :param target_index: 要计算的一行风险指标
        :return: 概率值和风险类型
        """
        # 归一化
        sum = 0
        for i in target_index[1]:
            sum += i
        for i in range(len(target_index[1])):
            target_index[1][i] = target_index[1][i] / sum
        # 查表计算
        # print(target_index[0])
        # print(target_index[1])
        # print(pointer_table)
        sum = 0
        for i in range(len(target_index[0])):
            for j in pointer_table:
                if target_index[0][i] == j[3]:
                    sum += target_index[1][i] * j[2]
                    break
        for i in pointer_table:
            if i[0] <= sum and sum < i[1]:
                return sum, i[3]

    def get_target_index_u11(self, file_name="RP2_U11.CSV"):
        # global U11
        U11 = self.U11
        target_index_u11 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u11)
        for i in range(1, lens):
            # print( target_index_u11[i][0])
            if (
                target_index_u11[i][0] <= float(U11)
                and float(U11) < target_index_u11[i][1]
            ):
                return [target_index_u11[0][2:], target_index_u11[i][2:]]
        return False

    def get_target_index_u12(self, file_name="RP2_U12.CSV"):
        # global U12,U09
        U12 = self.U12
        U09 = self.U09
        target_index_u12 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u12)
        if U09 == 0:
            area = json.loads(U12)["r"] ** 2 * math.pi
            for i in range(1, lens // 2):
                if target_index_u12[i][0] <= area and area < target_index_u12[i][1]:
                    return [target_index_u12[0][3:], target_index_u12[i][3:]]
        elif U09 == 1:
            area = json.loads(U12)["a"] * json.loads(U12)["b"]
            for i in range(lens // 2, lens):
                if target_index_u12[i][0] <= area and area < target_index_u12[i][1]:
                    return [target_index_u12[0][3:], target_index_u12[i][3:]]
        else:
            return False

    def get_target_index_u13(self, file_name="RP2_U13.CSV"):
        # global U13
        U13 = self.U13
        target_index_u13 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        return [target_index_u13[0][2:], target_index_u13[1][2:]]

    def get_target_index_u21(self, file_name="RP2_U21.CSV"):
        # global U21
        U21 = self.U21
        target_index_u21 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        return [target_index_u21[0][2:], target_index_u21[1][2:]]

    def get_target_index_u22(self, file_name="RP2_U22.CSV"):
        # global U22
        U22 = self.U22
        target_index_u22 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        return [target_index_u22[0][2:], target_index_u22[1][2:]]

    def get_target_index_u23(self, file_name="RP2_U23.CSV"):
        target_index_u23 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        return [target_index_u23[0][2:], target_index_u23[1][2:]]

    def get_target_index_u31(self, file_name="RP2_U31.CSV"):
        # global U31
        U31 = self.U31
        target_index_u31 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u31)
        for l in range(lens):
            if U31 == target_index_u31[l][0]:
                return [target_index_u31[0][1:], target_index_u31[l][1:]]
        return False

    def get_target_index_u32(self, file_name="RP2_U32.CSV"):
        # global U32
        U32 = self.U32
        target_index_u32 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u32)
        for l in range(lens):
            if U32 == target_index_u32[l][0]:
                return [target_index_u32[0][1:], target_index_u32[l][1:]]
        return False

    def get_target_index_u33(self, file_name="RP2_U33.CSV"):
        # global U33
        U33 = self.U33
        target_index_u33 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u33)
        for l in range(lens):
            if U33 == target_index_u33[l][0]:
                return [target_index_u33[0][1:], target_index_u33[l][1:]]
        return False

    def get_target_index_u34(self, file_name="RP2_U34.CSV"):
        # global U34
        U34 = self.U34
        target_index_u34 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u34)
        for l in range(lens):
            if U34 == target_index_u34[l][0]:
                return [target_index_u34[0][1:], target_index_u34[l][1:]]
        return False

    def get_target_index_u41(self, file_name="RP2_U41.CSV"):
        # global U4
        U4 = self.U4
        target_index_u41 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u41)
        U41 = json.loads(U4)["U41"]
        for i in range(1, lens):
            if target_index_u41[i][0] <= U41 and U41 < target_index_u41[i][1]:
                return [target_index_u41[0][2:], target_index_u41[i][2:]]
        return False

    def get_target_index_u42(self, file_name="RP2_U42.CSV"):
        # global U4
        U4 = self.U4
        target_index_u42 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u42)
        # print(json.loads(U4)['U42'])
        for i in range(1, lens):
            if target_index_u42[i][0] == json.loads(U4)["U42"]:
                return [target_index_u42[0][2:], target_index_u42[i][2:]]
        return False

    def get_target_index_u43(self, file_name="RP2_U43.CSV"):
        # global U4
        U4 = self.U4
        target_index_u43 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u43)
        U43 = json.loads(U4)["U43"]
        # print(json.loads(U4)['U43'])
        for i in range(1, lens):
            if target_index_u43[i][0] <= U43 and U43 < target_index_u43[i][1]:
                return [target_index_u43[0][2:], target_index_u43[i][2:]]
        return False

    def get_target_index_u51(self, file_name="RP2_U51.CSV"):
        # global U5
        U5 = self.U5
        target_index_u51 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u51)
        # U51 = sqrt(json.loads(U5)["U511"] ** 2 + json.loads(U5)["U512"] ** 2)
        U51 = json.loads(U5)["U51"]
        # print(U51)
        for i in range(1, lens):
            if target_index_u51[i][0] <= U51 and U51 < target_index_u51[i][1]:
                return [target_index_u51[0][2:], target_index_u51[i][2:]]
        return False

    def get_target_index_u52(self, file_name="RP2_U52.CSV"):
        # global U5
        U5 = self.U5
        target_index_u52 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u52)
        # print(json.loads(U5)['U52'])
        for i in range(1, lens):
            if target_index_u52[i][0] == json.loads(U5)["U52"]:
                return [target_index_u52[0][2:], target_index_u52[i][2:]]
        return False

    def get_target_index_u53(self, file_name="RP2_U53.CSV"):
        # global U5
        U5 = self.U5
        target_index_u53 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u53)
        # print(json.loads(U5)['U53'])
        for i in range(1, lens):
            if target_index_u53[i][0] == json.loads(U5)["U53"]:
                return [target_index_u53[0][2:], target_index_u53[i][2:]]
        return False

    def get_target_index_u54(self, file_name="RP2_U54.CSV"):
        # global U5
        U5 = self.U5
        target_index_u54 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u54)
        # print(json.loads(U5)['U54'])
        for i in range(1, lens):
            if target_index_u54[i][0] == json.loads(U5)["U54"]:
                return [target_index_u54[0][2:], target_index_u54[i][2:]]
        return False

    def get_target_index_u61(self, file_name="RP2_U61.CSV"):
        # global U6
        U6 = self.U6
        target_index_u61 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u61)
        for i in range(1, lens):
            if target_index_u61[i][0] == json.loads(U6)["U61"]:
                return [target_index_u61[0][2:], target_index_u61[i][2:]]
        return False

    def get_target_index_u62(self, file_name="RP2_U62.CSV"):
        # global U6
        U6 = self.U6
        target_index_u62 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u62)
        for i in range(1, lens):
            if (
                target_index_u62[i][0] <= json.loads(U6)["U62"]
                and json.loads(U6)["U62"] < target_index_u62[i][1]
            ):
                return [target_index_u62[0][2:], target_index_u62[i][2:]]
        return False

    def get_target_index_u63(self, file_name="RP2_U63.CSV"):
        U6 = self.U6
        target_index_u63 = self.lao.read_table_full(self.dir_path + "\\" + file_name)
        lens = len(target_index_u63)
        U63 = json.loads(U6)["U63"]
        for i in range(1, lens):
            if target_index_u63[i][0] <= U63 and U63 < target_index_u63[i][1]:
                return [target_index_u63[0][2:], target_index_u63[i][2:]]
        return False

    def CheckU4(self):
        if self.U4 == "" or self.U4 == None:
            return False
        else:
            return True

    def CheckU5(self):
        if self.U5 == "" or self.U5 == None:
            return False
        else:
            return True

    def CheckU6(self):
        if self.U6 == "" or self.U6 == None:
            return False
        else:
            return True

    # 工程编号 一级风险编号 二级风险编号 二级风险名称 风险权重 风险值 风险等级
    def calculate_second_risk_of_U1(self, risk_weight):
        list_of_secondrisk_of_U1 = []
        target_index_u11 = self.get_target_index_u11()
        u11_risk_value, u11_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u11
        )
        list_of_secondrisk_of_U1.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U1",
                "second_risk_id": "u11",
                "second_risk_name": self.second_risk_name["u11"],
                "second_risk_weight": risk_weight[0],
                "seccond_risk_value": u11_risk_value,
                "risk_classification": u11_risk_classification,
            }
        )
        target_index_u12 = self.get_target_index_u12()
        u12_risk_value, u12_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u12
        )
        list_of_secondrisk_of_U1.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U1",
                "second_risk_id": "u12",
                "second_risk_name": self.second_risk_name["u12"],
                "second_risk_weight": risk_weight[1],
                "seccond_risk_value": u12_risk_value,
                "risk_classification": u12_risk_classification,
            }
        )
        target_index_u13 = self.get_target_index_u13()
        u13_risk_value, u13_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u13
        )
        list_of_secondrisk_of_U1.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U1",
                "second_risk_id": "u13",
                "second_risk_name": self.second_risk_name["u13"],
                "second_risk_weight": risk_weight[0],
                "seccond_risk_value": u13_risk_value,
                "risk_classification": u13_risk_classification,
            }
        )
        return list_of_secondrisk_of_U1

    def calculate_second_risk_of_U2(self, risk_weight):
        list_of_secondrisk_of_U2 = []
        target_index_u21 = self.get_target_index_u21()
        u21_risk_value, u21_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u21
        )
        list_of_secondrisk_of_U2.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U2",
                "second_risk_id": "u21",
                "second_risk_name": self.second_risk_name["u21"],
                "second_risk_weight": risk_weight[0],
                "seccond_risk_value": u21_risk_value,
                "risk_classification": u21_risk_classification,
            }
        )

        target_index_u22 = self.get_target_index_u22()
        u22_risk_value, u22_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u22
        )
        list_of_secondrisk_of_U2.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U2",
                "second_risk_id": "u22",
                "second_risk_name": self.second_risk_name["u22"],
                "second_risk_weight": risk_weight[1],
                "seccond_risk_value": u22_risk_value,
                "risk_classification": u22_risk_classification,
            }
        )

        target_index_u23 = self.get_target_index_u23()
        u23_risk_value, u23_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u23
        )
        list_of_secondrisk_of_U2.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U2",
                "second_risk_id": "u23",
                "second_risk_name": self.second_risk_name["u23"],
                "second_risk_weight": risk_weight[2],
                "seccond_risk_value": u23_risk_value,
                "risk_classification": u23_risk_classification,
            }
        )
        return list_of_secondrisk_of_U2

    def calculate_second_risk_of_U3(self, risk_weight):
        list_of_secondrisk_of_U3 = []
        target_index_u31 = self.get_target_index_u31()
        u31_risk_value, u31_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u31
        )
        list_of_secondrisk_of_U3.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U3",
                "second_risk_id": "u31",
                "second_risk_name": self.second_risk_name["u31"],
                "second_risk_weight": risk_weight[0],
                "seccond_risk_value": u31_risk_value,
                "risk_classification": u31_risk_classification,
            }
        )

        target_index_u32 = self.get_target_index_u32()
        u32_risk_value, u32_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u32
        )
        list_of_secondrisk_of_U3.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U3",
                "second_risk_id": "u32",
                "second_risk_name": self.second_risk_name["u32"],
                "second_risk_weight": risk_weight[1],
                "seccond_risk_value": u32_risk_value,
                "risk_classification": u32_risk_classification,
            }
        )

        target_index_u33 = self.get_target_index_u33()
        u33_risk_value, u33_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u33
        )
        list_of_secondrisk_of_U3.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U3",
                "second_risk_id": "u33",
                "second_risk_name": self.second_risk_name["u33"],
                "second_risk_weight": risk_weight[2],
                "seccond_risk_value": u33_risk_value,
                "risk_classification": u33_risk_classification,
            }
        )

        target_index_u34 = self.get_target_index_u34()
        u34_risk_value, u34_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u34
        )
        list_of_secondrisk_of_U3.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U3",
                "second_risk_id": "u34",
                "second_risk_name": self.second_risk_name["u34"],
                "second_risk_weight": risk_weight[3],
                "seccond_risk_value": u34_risk_value,
                "risk_classification": u34_risk_classification,
            }
        )

        return list_of_secondrisk_of_U3

    def calculate_second_risk_of_U4(self, risk_weight):
        list_of_secondrisk_of_U4 = []

        target_index_u41 = self.get_target_index_u41()
        u41_risk_value, u41_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u41
        )
        list_of_secondrisk_of_U4.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U4",
                "second_risk_id": "u41",
                "second_risk_name": self.second_risk_name["u41"],
                "second_risk_weight": risk_weight[0],
                "seccond_risk_value": u41_risk_value,
                "risk_classification": u41_risk_classification,
            }
        )

        target_index_u42 = self.get_target_index_u42()
        u42_risk_value, u42_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u42
        )
        list_of_secondrisk_of_U4.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U4",
                "second_risk_id": "u42",
                "second_risk_name": self.second_risk_name["u42"],
                "second_risk_weight": risk_weight[1],
                "seccond_risk_value": u42_risk_value,
                "risk_classification": u42_risk_classification,
            }
        )

        target_index_u43 = self.get_target_index_u43()
        u43_risk_value, u43_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u43
        )
        list_of_secondrisk_of_U4.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U4",
                "second_risk_id": "u43",
                "second_risk_name": self.second_risk_name["u43"],
                "second_risk_weight": risk_weight[2],
                "seccond_risk_value": u43_risk_value,
                "risk_classification": u43_risk_classification,
            }
        )

        return list_of_secondrisk_of_U4

    def calculate_second_risk_of_U5(self, risk_weight):
        list_of_secondrisk_of_U5 = []

        target_index_u51 = self.get_target_index_u51()
        u51_risk_value, u51_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u51
        )
        list_of_secondrisk_of_U5.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U5",
                "second_risk_id": "u51",
                "second_risk_name": self.second_risk_name["u51"],
                "second_risk_weight": risk_weight[0],
                "seccond_risk_value": u51_risk_value,
                "risk_classification": u51_risk_classification,
            }
        )

        target_index_u52 = self.get_target_index_u52()
        u52_risk_value, u52_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u52
        )
        list_of_secondrisk_of_U5.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U5",
                "second_risk_id": "u52",
                "second_risk_name": self.second_risk_name["u52"],
                "second_risk_weight": risk_weight[1],
                "seccond_risk_value": u52_risk_value,
                "risk_classification": u52_risk_classification,
            }
        )

        target_index_u53 = self.get_target_index_u53()
        u53_risk_value, u53_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u53
        )
        list_of_secondrisk_of_U5.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U5",
                "second_risk_id": "u53",
                "second_risk_name": self.second_risk_name["u53"],
                "second_risk_weight": risk_weight[2],
                "seccond_risk_value": u53_risk_value,
                "risk_classification": u53_risk_classification,
            }
        )

        target_index_u54 = self.get_target_index_u54()
        u54_risk_value, u54_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u54
        )
        list_of_secondrisk_of_U5.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U5",
                "second_risk_id": "u54",
                "second_risk_name": self.second_risk_name["u54"],
                "second_risk_weight": risk_weight[3],
                "seccond_risk_value": u54_risk_value,
                "risk_classification": u54_risk_classification,
            }
        )
        return list_of_secondrisk_of_U5

    def calculate_second_risk_of_U6(self, risk_weight):
        list_of_secondrisk_of_U6 = []

        target_index_u61 = self.get_target_index_u61()
        u61_risk_value, u61_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u61
        )
        list_of_secondrisk_of_U6.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U6",
                "second_risk_id": "u61",
                "second_risk_name": self.second_risk_name["u61"],
                "second_risk_weight": risk_weight[0],
                "seccond_risk_value": u61_risk_value,
                "risk_classification": u61_risk_classification,
            }
        )

        target_index_u62 = self.get_target_index_u62()
        u62_risk_value, u62_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u62
        )
        list_of_secondrisk_of_U6.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U6",
                "second_risk_id": "u62",
                "second_risk_name": self.second_risk_name["u62"],
                "second_risk_weight": risk_weight[1],
                "seccond_risk_value": u62_risk_value,
                "risk_classification": u62_risk_classification,
            }
        )

        target_index_u63 = self.get_target_index_u63()
        u63_risk_value, u63_risk_classification = self.calculate_waverage_of_risk(
            self.pointer_table, target_index_u63
        )
        list_of_secondrisk_of_U6.append(
            {
                "process_id": self.U01,
                "first_risk_id": "U6",
                "second_risk_id": "u63",
                "second_risk_name": self.second_risk_name["u63"],
                "second_risk_weight": risk_weight[2],
                "seccond_risk_value": u63_risk_value,
                "risk_classification": u63_risk_classification,
            }
        )

        return list_of_secondrisk_of_U6

    def second_risk(self):
        print("secondrisk")
        print(self.matrix_B)
        list_second_risk = []
        list_second_risk += self.calculate_second_risk_of_U1(self.matrix_B[0])
        list_second_risk += self.calculate_second_risk_of_U2(self.matrix_B[1])
        list_second_risk += self.calculate_second_risk_of_U3(self.matrix_B[2])
        cur = 3
        if self.CheckU4():  # 判断U4-既有邻近地下柔性管线特性是否存在
            list_second_risk += self.calculate_second_risk_of_U4(self.matrix_B[cur])
            cur += 1
        if self.CheckU5():  # 判断U5-既有邻近地下刚性管线特性是否存在
            list_second_risk += self.calculate_second_risk_of_U5(self.matrix_B[cur])
            cur += 1
        if self.CheckU6():  # 判断U6-既有邻近基础特性是否存在
            list_second_risk += self.calculate_second_risk_of_U6(self.matrix_B[cur])

        return list_second_risk


"""
最后一个界面：一级风险编号，二级风险编号，二级风险名称，风险权重，风险等级
数据库：工程编号，二级风险编号	风险权重	风险值	风险等级
工程编号 一级风险编号 二级风险编号 二级风险名称 风险权重 风险值 风险等级
"""

'''
if __name__ == "__main__":
     matrix_group_B = [
         [0.33, 0.33, 0.33],
         [0.33, 0.33, 0.33],
         [0.25, 0.25, 0.25, 0.25],
         [0.25, 0.25, 0.25, 0.25],
         [0.33, 0.33, 0.33],
     ]
     a = [
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
             ]
     laolao = NewProjectInfo()
     A = laolao.calculate_matrix_A(a)
     B = laolao.calculate_matrix_B(matrix_group_B, A)

     for i in laolao.second_risk():
     print(i)
         '''