import tkinter

root = tkinter.Tk()
root.title('myapp')  # 不要写成root.title='myapp',这与c++窗体不同
root.geometry('500x300')
root.mainloop()
"""
    创建根窗体对象
        ①tkinter.Tk():创建一个根窗体对象。使用后会立即显示窗口，别忘记用root接收。
        ②root.title(name):设置根窗体的标题。
        ③root.geometry('aaaxbbb'):设置根窗体的尺寸。注意这里的乘号是小写字母x，aaa为宽，bbb为高。
        ④root.mainloop():监听上方代码，封锁下方代码，直到窗口被关闭。
"""