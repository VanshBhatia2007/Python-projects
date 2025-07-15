from tkinter import *
from time import strftime

Clock = Tk()
Clock.title("Digital Clock")
Clock.config(bg="black")

def clock():
    tick = strftime("%H:%M:%S:%p")
    label.config(text=tick)
    label.after(1000,clock)

label = Label(Clock, font=("segoe",60),fg="blue",bg="white")

label.pack(anchor= "center")

clock()
mainloop()

