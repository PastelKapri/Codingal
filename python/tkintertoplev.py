from tkinter import *

win = Tk()
win.title("mainwin")
win.geometry("300x200")

def topwin():
    top = Toplevel()
    top.title("Top Level Window")
    top.geometry("200x150")
    labeltop = Label(top, text="This is a top level window")
    labeltop.pack()
    top.mainloop()
labelmain = Label(win, text="This is the main window")
button = Button(win, text="Open Top Level Window", command=topwin)

labelmain.pack()
button.pack()

win.mainloop()