from tkinter import *
from PIL import Image, ImageTk

win = Tk()
win.title("img_test")
win.geometry("400x300")

upl = Image.open("C:/Users/Olive Kapri/Desktop/Projects/Codingal/python/Screenshot 2024-09-23 125543.png")

img = ImageTk.PhotoImage(upl)

label = Label(win, image=img, height=200, width=200)
label.pack()

win.mainloop()