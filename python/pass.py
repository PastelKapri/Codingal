from tkinter import *

win = Tk()
win.title("Password Generator")
win.geometry("400x300")


import string
import random

password = []
lenght = 12

for i  in range(lenght):
    ranchar = random.choice(string.ascii_letters + string.digits + string.punctuation)
    password.append(ranchar)
print("your password is " + "".join(password))

def generate_password():
    label2 = Label(text = "your password is " + "".join(password))
    label2.pack()

label1 = Label(text = "12 Charater Password Generator")
button1 = Button(text = "Generate Password", command = generate_password)


label1.pack()
button1.pack()


win.mainloop()