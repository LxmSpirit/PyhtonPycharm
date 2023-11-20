import tkinter
def func():
    print("小王是憨憨")
win = tkinter.Tk()# 创建主窗口
win.title("小王最帅")# 设置标题
win.geometry("400x400+200+50")#设置大写和位置
'''
Entry:输入控件，用于显示简单的文本内容
'''
entry1=tkinter.Entry(win,show='*') # show=‘*’可以表示输入的密码#，密文显示
entry1.pack()
e=tkinter.Variable()# 绑定变量
entry2=tkinter.Entry(win,textvariable=e) # show=‘*’可以表示输入的密码
entry2.pack()
e.set("放假放假")#e代表输入框这个对象，设置值
# 取值
print(e.get())
print(entry2.get())# 进入消息循环，可以写控件
win.mainloop()
"""
Entry控件
"""