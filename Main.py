# Main Run File
from tkinter import *
from Stage_One import Main
import os


def exitGame():
    root.quit()
    # delete keycard on game exit
    if os.path.exists("keycard.txt"):
        os.remove("keycard.txt")
    else:
        print("file already Deleted")

# root window
root = Tk()
root.geometry('180x180')
root.resizable(False, False)
root.title('Escape Room')

# Windows Text
mainMenu = Label(root, text='Main Menu')

# Start/Exit Game
start_button = Button(root, text='Start', command=lambda: Main(root))

exit_button = Button(root, text='Exit', command=lambda: exitGame())

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
