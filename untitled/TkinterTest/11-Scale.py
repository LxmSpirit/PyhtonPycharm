from tkinter import *

root = Tk()
root.geometry('500x300')

def getval(event):
    c = var.get()
    lb.configure(text=f'滑块的取值为{c}')
    return

if __name__ == '__main__':
    root.title('滑块实验')
    var = DoubleVar()
    sc = Scale(root, orient=HORIZONTAL, length=200, from_=1.0, to=5.0, label='请拖动滑块', tickinterval=1, resolution=0.05,
               variable=var)
    sc.pack()
    lb = Label(root, text='滑块取值为1')
    lb.pack()
    sc.bind('<ButtonRelease-1>', getval)
    root.mainloop()

"""
 滑块：(Scale)
    滑块(Scale)是一种直观地进行数值输入的交互控件。其主要属性见下表：
    属性	功能描述
    from_	起始值（最小可取值）
    lable	标签文字，默认为无
    length	滑块控件实例宽（水平方向）或 高（垂直方向），默认为100像素
    orient	滑块控件实例呈现方向，VERTCAL或HORIZONTAL(默认)
    repeatdelay	鼠标响应延时，默认为 300ms
    resolution	分辨精度，即最小值间隔
    sliderlength	滑块宽度，默认为30 像素
    state	状态，若设置 state=DISABLED,则滑块控件实例不可用
    tickinterval	标尺间隔，默认为0，若设置过小，则会重叠
    to	终止值(最大可取值)
    variable	返回数值， 类型可为IntVar(整数)、DoubleVar(浮点数)、或 StringVar(字符串)
    width	控件实例本身的宽度，默认为15像素

滑块控件实例的主要方法比较简单，有 get()和set(值) ，滑块控件实例的主要方法比较简单，有 get()和set(值)。
滑块实例也可绑定鼠标左键释放事件<ButtoonRelease-1>,并在执行函数中添加参数event来实现事件响应。注意是单括号‘<’,'>'，不是双括号‘<<’,'>>'。

"""