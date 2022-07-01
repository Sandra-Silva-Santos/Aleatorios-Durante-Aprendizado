from logging import root
from tkinter import Tk, Button, Label 
from tkinter.messagebox import showinfo
from time import strftime, localtime, time

def cliked():
    time = strftime('Day: %d %b %y\nTime: %H:%M:%S\n', localtime())
    showinfo(message=time)

root = Tk()
Button=Button(root, text='Click me', command=cliked)
Button.pack()
root.mainloop()

