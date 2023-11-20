import tkinter

root = tkinter.Tk()
lbred = tkinter.Label(root, text='1', fg='red', relief=tkinter.GROOVE)
lbred.pack()
lbgreen = tkinter.Label(root, text='2', fg='green', relief=tkinter.GROOVE)
lbgreen.pack(side=tkinter.LEFT) #参数 side 可取值：side=TOP(默认)，side=LEFT,side=RIGHT,side=BOTTOM,分别表示本控件实例的布局相对于下一个控件实例的方位。
lbblue = tkinter.Label(root, text='3', fg='blue', relief=tkinter.GROOVE)
lbblue.pack(fill=tkinter.BOTH) #参数fill 可取值：fill=X,fill=Y或fill=BOTH，分别表示允许控件向水平方向、垂直方向或二维方向将剩余空间填充满
root.mainloop()
"""
控件布局
    .pack()方法（用Label举例）
        ①tkinter.Label(root,..,text,fg,relief):创建一个标签对象。
            其中，root是根窗体；text是标签文本；fg是标签颜色，各种颜色用英文表示；relief是标签边缘属性，relief=tkinter.GROOVE为边缘凹陷属性。
            注意Label中L为大写。
        ②label.pack():将label放置在根窗体上。
            放置的规则为：如果不加参数的默认方式，将以不重叠且紧挨着的形式从上往下纵向排列，水平位置居中。
        ③label.pack()可设置fill和side等参数。
            其中，参数fill 可取值：fill=X,fill=Y或fill=BOTH，分别表示允许控件向水平方向、垂直方向或二维方向将剩余空间填充满。
            参数 side 可取值：side=TOP(默认)，side=LEFT,side=RIGHT,side=BOTTOM,分别表示本控件实例的布局相对于下一个控件实例的方位。
"""