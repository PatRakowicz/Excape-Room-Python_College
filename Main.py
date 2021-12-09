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

# Timer
end_time = time.time()
start_time = time.time()

# TODO click on exit door print final time
# print user time
total_time = end_time - start_time
print('you took ' + str(total_time) + ' to complete the escape room')

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
