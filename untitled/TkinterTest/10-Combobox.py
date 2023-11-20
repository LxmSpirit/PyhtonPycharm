from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('500x300')

def cul(event):  # 注意一定要传递一个参数，将来这个参数代表实例本身
    c = cb.current()
    try:
        a = float(input1.get())
        b = float(input2.get())
    except:
        return
    dict = {0: a + b, 1: a - b, 2: a * b, 3: a / b}
    lb.configure(text=str(dict.get(c)))
    return

if __name__ == '__main__':
    root.title('四则运算')
    input1 = Entry(root)
    input2 = Entry(root)
    input1.place(relx=0.1, rely=0.1)
    input2.place(relx=0.5, rely=0.1)
    cb = Combobox(root, values=['加', '减', '乘', '除'])
    cb.place(relx=0.1, rely=0.5)
    cb.bind('<<ComboboxSelected>>', cul)  # 设置复选框被选择的相应函数
    lb = Label(root)
    lb.place(relx=0.5, rely=0.5)
    root.mainloop()

"""
 . 组合框（Combobox）
    该控件并不包含在 tkinter 模块中，而是与 TreeView、Progressbar、Separator等控件一同包含在tkinter 的子模块ttk中。
        因此使用该控件前，应先from tkinter.ttk import *。

指定变量var=StringVar(),并设置实例属性 textvariable = var,values=[列表...]。
    组合框控件常用方法有：获得所选中的选项值get()和获得所选中的选项索引current()。
注：定义的cur()函数必须带一个参数，名字可以任意。因为当定义<<ComboboxSelected>>事件的相应函数时，也将实例cb传入了进去。
"""