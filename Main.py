# Main Run File
from tkinter import *
from Stage_One import Main
# from Stage_Two import Main

# TODO Timer

# root window
root = Tk()
root.geometry('250x200')
root.resizable(False, False)
root.title('Escape Room')

# Windows Text
EscapeRoom = Label(root, text='Main Menu')

# Start game
start_button = Button(root, text='Start', command=lambda: Main(root))

# Exit Game
exit_button = Button(root, text='Exit', command=lambda: root.quit())

# All packing for Main
EscapeRoom.pack()
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
