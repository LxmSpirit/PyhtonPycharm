from tkinter import *
import time

root = Tk()
root.geometry('500x300')


def gettime():
    nowtime = time.strftime("%H:%M:%S")
    # lb.configure(text=nowtime,fg='green')
    var.set(nowtime)
    root.after(1000, gettime)  # 1000ms后调用gettime()函数


if __name__ == '__main__':
    root.title('time')
    var = StringVar()  # 创建一个特殊变量对象
    lb = Label(root, textvariable=var, fg='red', font=('微软雅新', 80))  # 注意这里定义Label时定义textvariable而不是text
    lb.pack()
    gettime()
    root.mainloop()