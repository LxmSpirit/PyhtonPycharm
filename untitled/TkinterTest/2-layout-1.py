import tkinter

root = tkinter.Tk()
root.title('myapp')  # 不要写成root.title='myapp',这与c++窗体不同
root.geometry('500x300')
msg1 = tkinter.Message(root, text='我是一行文字我是另一行文字', relief=tkinter.GROOVE)
msg1.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.4)
root.mainloop()

"""
 .grid()方法
    基于表格布局，在相应表格中放置放置控件。其中一些参数意义如下：
    ①column,row：控件的行、列坐标，默认为0（注意坐标从0开始）。
    ②columnspan,rowspan：控件跨越的行数、列数，默认为1
    ③ipadx,ipady：实例控件所呈现区域内的像素数，定义控件的大小。
    ④padx,pady：实例控件所在单元格的大小，定义单元格的大小。
 .place()方法
    根据空间在父容器中的相对位置进行布局：
    ①x,y：控件相对于根窗体下的坐标。
    ②relx,rely：控件相对与根窗体下的相对位置。
    ③height和width：控件的高度和宽度。（单位为像素）。
    ④relheight和relwidth：控件相对于根窗体的相对高度和宽度。
注：可以和grid()方法混合使用
"""