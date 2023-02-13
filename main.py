from tkinter import *
import time

root = Tk()
root.geometry("400x300")
root.title("Dre's Clock")
root.config(bg="black")


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    time_label.config(text= hour + ":" + minute + ":" + second, font=("Helvetica",50))
    time_label.update()
    time_label.after(1000, clock)


def update():
    time_label.config(text="new text")


time_label = Label(root, text="", font=("Helvetica", 50), fg="red", bg="black")
time_label.pack(expand=True)

clock()

root.mainloop()
