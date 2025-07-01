from tkinter import *

win = Tk()
win.title("test_win")
win.geometry("400x300")

label1 = Label(text = "Hi this is test label", bg  = "blue")
button1 = Button(text = "Click Me", bg = "red", fg = "white")
entry1 = Entry(bg = "green", fg = "black", width= 50)

label1.pack()
button1.pack()
entry1.pack()

frame = Frame(master = win, relief = RAISED, bg = "yellow", borderwidth = 5)
frame.pack()
label2 = Label(master = frame, text = "This is a label inside a frame", bg = "yellow")
label2.pack()
text1 = Text(master = win, height = 5, width = 30, bg = "pink", fg = "black")
text1.pack()
win.mainloop()