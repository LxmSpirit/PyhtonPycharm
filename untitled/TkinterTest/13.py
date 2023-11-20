import tkinter
# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("小王最帅")
#设置大写和位置
win.geometry("400x400+200+50")
def showinfo():
    # 获取输入的内容
    print(entry.get())
entry=tkinter.Entry(win)
entry.pack()
button=tkinter.Button(win,text="按钮",command=showinfo)
button.pack()
# 进入消息循环，可以写控件
win.mainloop()
"""
点击按钮输出输入框中的内容
"""