# Stage One
from tkinter import *


# TODO Stage One
#   Create Exit (work in progress) - pat
#   Create safe
#   Create Random boxes
#   Create shelf with key-card

def exitStage(*args):
    global code_entry
    x = Toplevel()
    code_entry = Entry(x)
    code_entry.pack()
    button = Button(x, text='Enter', command=lx)
    button.pack()
    # TODO Close window
    #   Print 'Game Complete'
    # I think we need to move this stuff below outside of this function
    newWindow = Toplevel()
    newWindow.geometry('100x100')
    newWindow.resizable(False, False)
    canvas = Canvas(newWindow)
    canvas.create_text(50, 50, text='Game Complete!', fill='black', font='Helvetica 15 bold')


def safeClick(*args):
    global entry
    x = Toplevel()
    entry = Entry(x)
    entry.pack()
    button = Button(x, text='Enter', command=fx)
    button.pack()

# opens keycard.txt which contains 'keycard.ex'
def crateClick():
    key_file = open('keycard.txt')
    print(key_file.read())
    key_file.close()
    


# safe click action
def fx():
    # checks for valid 'keycard' input if correct displays code if not clears entry box and displays error
    key = entry.get()
    if key == 'keycard.ex':
        messagebox.showinfo('Code', '1776')
    else:
        entry.delete('0', 'end)
        messagebox.showwarning('Error', 'Invalid input')
# exit door button action
def lx():
    exit_code = code_entry.get()
    if exit_code == '1776':
                     # not sure if a variable can be included in a message box
        messagebox.showinfo('Congratulations', 'you completed the escape room in' + str(final_time))
    else:
        code_entry.delete('0', 'end)
        messagebox.showwarning('Error', 'Invalid input')

# Everything goes in here
def Main(root):
    # Stage One Window Create
    newWindow = Toplevel(root)
    canvas = Canvas(newWindow)
    newWindow.resizable(False, False)

    newWindow.title('Stage One')
    newWindow.geometry('500x500')

    # Exit Door
    canvas.create_rectangle(225, 5, 275, 55, fill='black', tag='exitDoor')
    canvas.create_text(250, 70, text="Exit", fill="black", font='Helvetica 15 bold')
    canvas.tag_bind('exitDoor', '<Button-1>', exitStage)

    # Safe
    canvas.create_rectangle(0, 215, 50, 270, fill='gray', tag='safe')
    canvas.create_text(25, 200, text="Safe", fill="black", font='Helvetica 15 bold')
    canvas.tag_bind('safe', '<Button-1>', safeClick)

    # Crate w/ Keycard
    canvas.create_rectangle(400, 425, 495, 475, fill='blue', tag='crate')
    canvas.create_text(445, 415, text='Crate', fill='black', font='Helvetica 15 bold')
    canvas.tag_bind('create', '<Button-1>', crateClick)

    # Packing
    canvas.pack(fill="both", expand=True)

    newWindow.mainloop()
