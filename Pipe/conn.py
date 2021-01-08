import pandas as pd
from sqlalchemy import  create_engine
import pymysql
import sys

conn=pymysql.connect("127.0.0.1","root","123456","pipeconstruction_riskaccessment")
cur=conn.cursor()
def chenk():
    sql="select * from Login"
    cur.execute(sql)
    a=cur.fetchall()
    print(a)

def insert(username,password):
    sql="insert into Login (username,password) values ('%s','%s')" % (username,password)
    cur.execute(sql)
    conn.commit()

def InsertInput(U01,U02,U03,U04,U31,U05,U32,U06,U33,U07,U34,U08,U11,U09,U12,U13,U4,U5,U6,U7):
    # print('here Iuput')
    # print(U01, U02, U03, U04, U31, U05, U32, U06, U33, U07, U34, U08, U11, U09, U12, U13, U4, U5, U6, U7)
    sql = "insert into newprojectinfo (U01,U02,U03,U04,U31,U05,U32,U06,U33,U07,U34,U08,U11,U09,U12,U13,U4,U5,U6,U7) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') " % (U01,U02,U03,U04,U31,U05,U32,U06,U33,U07,U34,U08,U11,U09,U12,U13,U4,U5,U6,U7)

    cur.execute(sql)
    conn.commit()

def LoginChenk(username,password):
    sql = "select * from Login"
    cur.execute(sql)
    a = cur.fetchall()
    if a[1]==username & a[2]==password :
        return True
    else:
        return False

def Check_username(username):
    sql="select username from Login where username ='%s'" % username
    cur.execute(sql)
    a = cur.fetchall()
    if len(a) == 0:
        return True
    else:
        return False
def Chenk_password(username,password):
    sql="select password from Login where username= '%s'" % username
    cur.execute(sql)
    a=cur.fetchall()
    if a[0][0] == password:
        return True
    else:
        return False
def Login(username,password):
    a = Check_username(username)
    if a:
        print('用户名错误')
        return False

    else:
        b=Chenk_password(username,password)
        if b:
            print("登录成功")
            return True

        else:
            print('密码错误')
            return False
