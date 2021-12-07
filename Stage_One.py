from tkinter import *

root = Tk()

window = root.geometry('100x100')

label = Label(window, text="a generic Toplevel window")
label.pack()

root.mainloop()
