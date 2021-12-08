# Stage One
from tkinter import *


# TODO Stage One
#   Create Exit (work in progress) - pat
#   Create safe
#   Create Random boxes
#   Create shelf with key-card

def clicked(*args):
    print('box Clicked')


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

    newWindow.mainloop()
