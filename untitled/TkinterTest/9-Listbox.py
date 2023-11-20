from tkinter import *

root = Tk()
root.geometry('500x300')

def init():
    list = ['数学', '物理', '化学', '语文', '外语']
    listbox.delete(0, END)
    for item in list:
        listbox.insert(END, item)
    return

def insert():
    if entry.get() != '':
        if listbox.curselection() != ():
            id = listbox.curselection()[0]
            listbox.insert(id, entry.get())
        else:
            listbox.insert(END, entry.get())
    return

def change():
    if entry.get() != '':
        if listbox.curselection() != ():
            id = listbox.curselection()[0]
            listbox.delete(id)
            listbox.insert(id, entry.get())
    return

def delete():
    if listbox.curselection() != ():
        listbox.delete(listbox.curselection())
    return

def clear():
    listbox.delete(0, END)
    return

if __name__ == '__main__':
    root.title('列表框实验')
    fm1 = Frame(root)#布局
    fm2 = Frame(root)
    fm1.place(relx=0.0)
    fm2.place(relx=0.5)
    listbox = Listbox(fm1)
    listbox.pack()
    entry = Entry(fm2)
    entry.pack()
    btn1 = Button(fm2, text='初始化', command=init)
    btn2 = Button(fm2, text='插入', command=insert)
    btn3 = Button(fm2, text='修改', command=change)
    btn4 = Button(fm2, text='删除', command=delete)
    btn5 = Button(fm2, text='清空', command=clear)
    btn1.pack(fill=X)
    btn2.pack(fill=X)
    btn3.pack(fill=X)
    btn4.pack(fill=X)
    btn5.pack(fill=X)
    root.mainloop()

"""
 . 列表框（Listbox）
    方法	功能描述
    curselection()	返回光标选中项目编号的元组，注意并不是单个的整数
    delete(起始位置，终止位置)	删除项目，终止位置可省略，全部清空为delete(0,END)
    get(起始位置，终止位)	返回范围所含项目文本的元组，终止位置可忽略
    insert(位置，项目元素)	插入项目元素（若有多项，可用列表或元组类型赋值），若位置为END，则将项目元素添加在最后
    size()	返回列表框行数
列表框实质上就是将Python 的列表类型数据可视化呈现，在程序实现时，也可直接对相关列表数据进行操作，然后再通过列表框展示出来 。

"""