import random
from tkinter import *
from tkinter.font import BOLD

def boardLayout():
    global w
    label.config(text="Game begins with "+w)
    for row in range(3):
        for column in range(3):
            a[row][column].config(text=".",bg="white", state=NORMAL,font=BOLD)

def chance(i,j):
    global w
    a[i][j].config(text=w)
    a[i][j].config(state=DISABLED)
    if w=="X":
        w="O"
    else:
        w="X"
    label.config(text="Chance of "+w)
    c=checkWinCondition()
    if(c==1 and checkFull()==1):
        label.config(text="Match Draw!")
def checkFull():
    for i in range (3):
        for j in range(3):
            if(a[i][j]["text"]=="."):
                return 0
    return 1
def checkWinCondition():
    if(a[0][0]["text"]==a[0][1]["text"]==a[0][2]["text"]!="."):
        a[0][0].config(bg="green")
        a[0][1].config(bg="green")
        a[0][2].config(bg="green")
        disableButtons()
        label.config(text="Game over."+a[0][0]["text"]+" wins!")
        return 0
    elif (a[0][0]["text"]==a[1][0]["text"]==a[2][0]["text"]!="."):
        a[0][0].config(bg="green")
        a[1][0].config(bg="green")
        a[2][0].config(bg="green")
        disableButtons()
        label.config(text="Game over."+a[0][0]["text"]+" wins!")
        return 0
    elif (a[0][0]["text"]==a[1][1]["text"]==a[2][2]["text"]!="."):
        a[0][0].config(bg="green")
        a[1][1].config(bg="green")
        a[2][2].config(bg="green")
        disableButtons()
        label.config(text="Game over."+a[0][0]["text"]+" wins!")
        return 0
    elif (a[1][0]["text"]==a[1][1]["text"]==a[1][2]["text"]!="."):
        a[1][0].config(bg="green")
        a[1][1].config(bg="green")
        a[1][2].config(bg="green")
        disableButtons()
        label.config(text="Game over."+a[1][0]["text"]+" wins!")
        return 0
    elif (a[2][0]["text"]==a[2][1]["text"]==a[2][2]["text"]!="."):
        a[2][0].config(bg="green")
        a[2][1].config(bg="green")
        a[2][2].config(bg="green")
        disableButtons()
        label.config(text="Game over."+a[2][0]["text"]+" wins!")
        return 0
    elif (a[0][2]["text"]==a[1][1]["text"]==a[2][0]["text"]!="."):
        a[0][2].config(bg="green")
        a[1][1].config(bg="green")
        a[2][0].config(bg="green")
        disableButtons()
        label.config(text="Game over."+a[0][2]["text"]+" wins!")
        return 0
    elif (a[0][1]["text"]==a[1][1]["text"]==a[2][1]["text"]!="."):
        a[0][1].config(bg="green")
        a[1][1].config(bg="green")
        a[2][1].config(bg="green")
        disableButtons()
        label.config(text="Game over."+a[0][1]["text"]+" wins!")
        return 0
    elif (a[0][2]["text"]==a[1][2]["text"]==a[2][2]["text"]!="."):
        a[2][2].config(bg="green")
        a[0][2].config(bg="green")
        a[1][2].config(bg="green")
        disableButtons()
        label.config(text="Game over."+a[0][2]["text"]+" wins!")
        return 0
    return 1
def toss():
    d=random.randint(0,1)
    if(d==0):
        return "O"
    else:
        return "X"

def play():
    global w
    w=toss()
    boardLayout()

def disableButtons():
    for i in range(3):
        for j in range(3):
            a[i][j].config(state=DISABLED)
                   
a= [[0,0,0],
    [0,0,0],
    [0,0,0]]

window = Tk()
window.title("Multiplayer")
window.geometry("250x230")


label = Label(text=" ", font=('Snap ITC',15))
label.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        a[row][column] = Button(frame, text=".",font=('Nordic Light',40), width=5, height=2,command=lambda row=row,column=column: chance(row,column))
        a[row][column].grid(row=row,column=column)

reset_button = Button(text="restart", font=('Baskerville Old Face',15), command=play)
reset_button.pack(side="top")
window.resizable(False,False)

play()
window.mainloop()