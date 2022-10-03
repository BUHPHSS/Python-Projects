from tkinter import *
import time

a=Tk()
a.title("Digital Clock")
#a.iconbitmap("clock.ico")

def dc():
    time1= time.strftime("%H:%M:%S")
    current_time.config(text=time1)
    current_time.after(250,dc)

digiClock=Label(a,text="Clock",font=("arial",25,"bold"),bg="blue",fg="white")
digiClock.grid(row=0,column=0)
current_time=Label(a,font=("times new roman",40,"bold"),bg="blue",fg="white")
current_time.grid(row=1,column=0)
dc()

a.mainloop()