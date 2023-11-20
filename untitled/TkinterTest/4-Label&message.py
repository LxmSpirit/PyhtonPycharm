from tkinter import *
import time

root = Tk()
root.geometry('500x300')


def gettime():
    nowtime = time.strftime("%H:%M:%S")
    lb.config(text=nowtime)
    root.after(1000, gettime)  # 1000ms后调用gettime()函数


if __name__ == '__main__':
    root.title('time')
    lb = Label(root, text='', fg='red', font=('微软雅新', 80))
    lb.pack()
    gettime()
    root.mainloop()

"""
文本输入和输出相关控件
        .标签(Label)和消息(Message)：Label显示单行文本，Message显示多行文本。其余属性基本一致。
        text属性只能用于第一次呈现时的固定文本。若需文本变更，有以下两种方法：
        ①用configure()方法改变text的值；
        ②定义tkinter的内部类型变量var=StringVar()，改变其值也可使文本发生变化。
        方法一：用configure()方法改变text的值 
            注：样例中用了config()，实际上configure()有同样作用。关于它们的差别，在使用中没有找出差别，网上资料查找也无果。
        方法二：利用textvariable变量属性来实现文本变化。
"""