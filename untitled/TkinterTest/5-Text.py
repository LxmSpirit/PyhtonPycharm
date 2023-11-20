from tkinter import *
import time
import datetime

root = Tk()
root.geometry('500x300')

def gettime():
    nowtime = str(datetime.datetime.now()) + '\n'
    txt.insert(END, nowtime)
    root.after(1000, gettime)  # 1000ms后调用gettime()函数

if __name__ == '__main__':
    root.title('timetext')
    txt = Text(root)
    txt.pack()
    gettime()
    root.mainloop()

"""
.文本框（Text）
    文本框方法如下：
    方法	功能
    delete(起始位置，[,终止位置])	删除指定区域文本
    get(起始位置，[,终止位置])	获取指定区域文本
    insert(位置，[,字符串]...)	将文本插入到指定位置
    see(位置)	在指定位置是否可见文本，返回布尔值
    index(标记)	返回标记所在的行和列
    mark_names()	返回所有标记名称
    mark_set(标记，位置)	在指定位置设置标记
    mark_unset(标记)	去除标记
上表位置的取值可为整数，浮点数或END（末尾），例如0.0表示第0列第0行
.输入框（Entry）：接受单行文本输入的控件。通常只用get()和delete()两个方法，delete(0,END)可清空输入框。
"""