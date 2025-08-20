from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

win = Tk()
win.title("Denominator Calculator")
win.geometry("700x500")

upload_img = Image.open("C:/Users/Olive Kapri/Desktop/Projects/Codingal/python/temp.webp")  
img = ImageTk.PhotoImage(upload_img)

img_label = Label(win, image=img, height=200, width=200)
img_label.place(x=250, y=20)

label1  = Label(win, text="Welcome to the Denominator Calculator", font=("Arial", 20), fg="blue")
label1.place(x=150, y=250)

def msg():
    msg_box = messagebox.showinfo("Info", "Do you want to use the denominator calculator?")
    if msg_box == "ok":
        toplev()

button = Button(win, text="Click to start calculator", command=msg, font=("Arial", 15), bg="lightblue")
button.place(x=250, y=300)

def toplev():
    top = Toplevel()
    top.geometry("500x500")
    top.title("Denominator Calculator")

    label_top = Label(top, text="Enter amount", font=("Arial", 12))
    entry = Entry(top, font=("Arial", 12)) 

    lb = Label(top, text="Here are the notes:")

    l1 = Label(top, text="200")
    l2 = Label(top, text="100")
    l3 = Label(top, text="50")
    l4 = Label(top, text="20")

    t1 = Entry(top, font=("Arial", 12))
    t2 = Entry(top, font=("Arial", 12))
    t3 = Entry(top, font=("Arial", 12))
    t4 = Entry(top, font=("Arial", 12))

    def cal():
        try:
            global amount
            amount = int(entry.get())
            note200 = amount // 200
            amount % 200
            note100 = amount // 100
            amount % 100
            note50 = amount // 50
            amount % 50
            note20 = amount // 20
            amount % 20

            t3.delete(0, END)
            t2.delete(0, END)
            t1.delete(0, END)
            t4.delete(0,END)

            t1.insert(str(0, note200))
            t2.insert(str(0, note100))
            t3.insert(str(0, note50))
            t4.insert(str(0, note20))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    btn = Button(top, text="Calculate",command=cal, font=("Arial", 15), bg="lightblue")

    label_top.place(x=230, y=50 )

    entry.place(x=200, y=80 )

    btn.place(x=240, y=120 )

    lb.place(x=140, y=170 )

    l1.place(x=180, y=200 )

    l2.place(x=180, y=230 )

    l3.place(x=180, y=260 )

    l4.place(x=180, y=290)
    



    t1.place(x=270, y=200 )

    t2.place(x=270, y=230 )

    t3.place(x=270, y=260)
    
    t4.place(x=270, y=290)

    top.mainloop()

win.mainloop()