from tkinter import *


def Main(root):
    newWindow = Toplevel(root)
    newWindow.title('Stage One')
    newWindow.geometry('400x400')
    Label(newWindow, text='Start import').pack()
    newWindow.mainloop()

    pass
