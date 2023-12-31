from tkinter import *


def Mysel():
    dic = {0: '甲', 1: '乙', 2: '丙'}
    s = "您选了" + dic.get(var.get()) + "项"
    lb.config(text=s)

root = Tk()
root.title('单选按钮')
lb = Label(root)
lb.pack()

var = IntVar()
rd1 = Radiobutton(root, text="甲", variable=var, value=0, command=Mysel)
rd1.pack()

rd2 = Radiobutton(root, text="乙", variable=var, value=1, command=Mysel)
rd2.pack()

rd3 = Radiobutton(root, text="丙", variable=var, value=2, command=Mysel)
rd3.pack()

root.mainloop()

"""
单选按钮(Radiobutton)
    排除具有共有属性外，还具有显示文本（text）、返回变量（variable）、返回值（value）、响应函数名（command）等重要属性。
        响应函数名“command=函数名”的用法与Button相同，函数名最后不要加括号。
    返回变量variable=var通常应预先声明变量的类型var=IntVar()或var=StringVar(),在所调用的函数中方可用var.get()方法获取被选中实例的value值。
"""