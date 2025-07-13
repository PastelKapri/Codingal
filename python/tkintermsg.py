from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Message Box Example")
win.geometry("300x200")

def msg():
    messagebox.showinfo("info_test", "This is a message box test")

button = Button(win,text="Click Me", command=msg)
button.place(x=100, y=80)

win.mainloop()