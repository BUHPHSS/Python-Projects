from tkinter import *

def single():
    w.destroy()
    import SinglePlayer

def multi():
    w.destroy()
    import Multiplayer

w = Tk()
w.title("Tic-Tac-Toe")
w.geometry("250x120")


l = Label(text="Main Menu", font=('Snap ITC',15))
l.pack(side="top")

f = Frame(w)
f.pack()

sPbutton = Button(text="Single Player", font=('Baskerville Old Face',15), command=single)
sPbutton.pack(side="top")
mPbutton = Button(text="Multiplayer mode", font=('Baskerville Old Face',15), command=multi)
mPbutton.pack(side="top")
w.resizable(False,False)
w.mainloop()