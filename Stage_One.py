# Stage One
from tkinter import *
from tkinter import messagebox
import time
import os
import random

# start timer
start_time = time.time()

# Random 4 Digit Number
fDigitNum = random.randint(1000, 9999)


def exitStage(*args):
    global code_entry
    x = Toplevel()
    code_entry = Entry(x)
    x.geometry('270x50')
    x.resizable(False, False)
    x.title('Pass Code')
    button = Button(x, text='Enter', command=exitDoor)

    code_entry.pack()
    button.pack()


# Click on safe and have user input keycard.txt for exit door passcode
def safeClick(*args):
    global entry
    x = Toplevel()
    entry = Entry(x)
    keycardRequired = Label(x, text='Keycard Required')
    button = Button(x, text='Enter', command=keycardCheck)

    keycardRequired.pack()
    entry.pack()
    button.pack()


# make keycard.txt with content for safe
def crateClick(*args):
    print('crate click')
    # check if file exists, if not creates file with parameters keycard.ex
    if not os.path.exists("keycard.txt"):
        key_file = open('keycard.txt', 'w+')
        key_file.write("keycard.ex")
        key_file.close()
    else:
        print("file already exists")


# safe click action
def keycardCheck():
    # checks for valid 'keycard' input if correct displays code if not clears entry box and displays error
    print(fDigitNum)
    with open(entry.get()) as f:
        line = f.readline()
        if line == 'keycard.ex':
            messagebox.showinfo('Exit #', str(fDigitNum))
        else:
            entry.delete('0', 'end')
            messagebox.showwarning('Error', 'Invalid input or Keycard Missing')


# exit door button action
def exitDoor():
    exit_code = code_entry.get()
    print(fDigitNum)
    if exit_code == str(fDigitNum):
        # end timer + calculate final time
        end_time = time.time()
        final_time = end_time - start_time
        # not sure if a variable can be included in a message box
        messagebox.showinfo('Congratulations!', 'You completed the escape room in ' + str(final_time))
        messagebox.showinfo('Exit Game', 'Use exit box in Main Menu to exit game')
    else:
        code_entry.delete('0', 'end')
        messagebox.showwarning('Error', 'Invalid input or Wrong Password')


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
    canvas.tag_bind('crate', '<Button-1>', crateClick)

    # Random Crate
    # Random Crate 2
    # Random Crate 3

    # Packing
    canvas.pack(fill="both", expand=True)

    newWindow.mainloop()
