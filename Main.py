# Main Run File
import Stage_One
import Stage_Two
from tkinter import *


root = Tk()

root.geometry('500x500')

Label(root, text='Escape Room')

btn = Button(root, text='Start Game', command=Stage_One)
btn.pack(side='top')
btn_2 = Button(root, text='Exit Game', bd='5', command=root.destroy)
btn_2.pack(side='bottom')

root.mainloop()
