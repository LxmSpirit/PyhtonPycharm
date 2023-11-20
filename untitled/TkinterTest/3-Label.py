from tkinter import *
root=Tk()
lb = Label(root,text='hello world!',
        bg='red',
        fg='green',
        font=('微软雅新',32),
        relief=GROOVE,
        width=20,
        height=2)
lb.pack()
root.mainloop()

"""
控件	名称	作用
Button	按钮	单击触发事件
Canvas	画布	绘制图形或绘制特殊控件
Checkbutton	复选框	多项选择
Entry	输入框	接收单行文本输入
Frame	框架	用于控件分组
Label	标签	单行文本显示
Listbox	列表框	显示文本列表
Menu      	菜单	创建菜单命令
Message	消息	多行文本标签，与Label 用法类似
Radiobutton	单选框	从互斥的多个选项中做单项选择
Scale	滑块 	鼠标拖动数值变化
Scrollbar	滑动条	即滚动条
Text	文本框	接受或输出显示多行文本
Toplevel	新建窗体容器	在顶层新建窗体容器

"""


"""
属性 	说明	取值
anchor	文本的起始位置	CENTER(默认)，E,S,W,N,NE,SE,SW,NW
bg	背景色	'red','green'等
bd	加粗	无
cursor	鼠标悬停光标	-
font	字体	例如：('华文新魏',32)
fg        	前景色	'red','green'等
height	高（文本控件单位为行，不是像素）	数字
image	显示图像	无
justify	多行文本对齐方式	CENTER(默认)，LEFT,RIGHT,TOP,BOTTOM
padx	水平扩展像素	无
pady	垂直扩展像素	无
relief	边界样式	FLAT,RAISED,SUNKEN,GROOVE,RIDGE
state	控件实例状态是否可用	NORMAL(默认)，DISABLED
width	宽(文本控件的单位为行，不是像素)	无

注：width和height单位为列或行，这是因为用pack()或grid()放置时按表格的单位给出。若用place()放置，可以在place参数中设置其控件大小，此时单位为像素。
"""