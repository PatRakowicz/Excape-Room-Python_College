# Stage One
from tkinter import *


# TODO Stage One
#   Create Exit (work in progress) - pat
#   Create safe
#   Create Random boxes
#   Create shelf with key-card

def clicked(*args):
    print('box Clicked')


def safe_click(*args):
    global entry
    x = Toplevel()
    canvas_two = Canvas(x, width=500, height=500)
    entry = Entry(x)
    entry.pack()
    button = Button(x, text='Enter', command=fx)
    button.pack()


# safe click action 
def fx():
    key = entry.get()
    print(key)


# Everything goes in here
def Main(root):
    global canvas
    # Stage One Window Create
    newWindow = Toplevel(root)
    canvas = Canvas(newWindow)
    newWindow.resizable(False, False)

    newWindow.title('Stage One')
    newWindow.geometry('500x500')

    # Click Box | Display box clicked
    canvas.create_rectangle(225, 5, 275, 55, fill='black', tag='exitDoor')
    canvas.tag_bind('exitDoor', '<Button-1>', clicked)

    # Packing
    canvas.pack(fill="both", expand=True)

    # safe
    safe = canvas.create_rectangle(0, 215, 50, 270, fill='gray', tag='safe')
    canvas.create_text(25, 200, text="Safe", fill="black", font=('Helvetica 15 bold'))
    canvas.tag_bind('safe', '<Button-1>', safe_click)

    newWindow.mainloop()
