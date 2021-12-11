# Main Run File
from tkinter import *
from Stage_One import Main
import time

# from Stage_Two import Main

# root window
root = Tk()
root.geometry('180x180')
root.resizable(False, False)
root.title('Escape Room')

# Windows Text
mainMenu = Label(root, text='Main Menu')

# Start/Exit Game
start_button = Button(root, text='Start', command=lambda: Main(root))



exit_button = Button(root, text='Exit', command=lambda: root.quit())

# TODO click on exit door print final time
# print user time

# All packing for Main
mainMenu.pack()
start_button.pack(
    ipadx=3,
    ipady=3,
    expand=True
)
exit_button.pack(
    ipadx=3,
    ipady=3,
    expand=True
)

root.mainloop()
