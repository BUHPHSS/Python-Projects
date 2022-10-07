import random
from tkinter import *
from tkinter.font import BOLD


def boardLayout():
    global player
    global b
    for row in range(3):
        for column in range(3):
            a[row][column].config(text=".",bg="white", state=NORMAL,font=BOLD)
    if player=="X":
        label.config(text="Player: X")
    else:
        label.config(text="Computer: X")
        if winMove(b)==0:
            if blockMove(b)==0:
                if foresight(b)==0:
                    randomMove(b)

def chance(i,j):
    global player
    global b
    a[i][j].config(text=player)
    a[i][j].config(state=DISABLED)
    c=checkWinCondition()
    if(c==1 and checkFull()==1):
        label.config(text="Match Draw!")
    elif c==1:
        if winMove(b)==0:
            if blockMove(b)==0:
                if foresight(b)==0:
                    randomMove(b)
        checkWinCondition()
            

def checkFull():
    for i in range (3):
        for j in range(3):
            if(a[i][j]["text"]=="."):
                return 0
    return 1

def winMove(b):
    if a[0][0]["text"]==a[0][1]["text"]==b and a[0][2]["text"]==".":
        a[0][2].config(text=b,state=DISABLED)
        return 1
    elif a[0][0]["text"]==a[0][2]["text"]==b and a[0][1]["text"]==".":
        a[0][1].config(text=b,state=DISABLED)
        return 1
    elif a[0][1]["text"]==a[0][2]["text"]==b and a[0][0]["text"]==".":
        a[0][0].config(text=b,state=DISABLED)
        return 1

    elif (a[0][0]["text"]==a[1][0]["text"]==b and a[2][0]["text"]=="."):
        a[2][0].config(text=b,state=DISABLED)
        return 1
    elif a[0][0]["text"]==a[2][0]["text"]==b and a[1][0]["text"]==".":
        a[1][0].config(text=b,state=DISABLED)
        return 1
    elif a[1][0]["text"]==a[2][0]["text"]==b and a[0][0]["text"]==".":
        a[0][0].config(text=b,state=DISABLED)
        return 1
        
    elif (a[0][0]["text"]==a[1][1]["text"]==b and a[2][2]["text"]=="."):
        a[2][2].config(text=b,state=DISABLED)
        return 1
    elif a[0][0]["text"]==a[2][2]["text"]==b and a[1][1]["text"]==".":
        a[1][1].config(text=b,state=DISABLED)
        return 1
    elif a[1][1]["text"]==a[2][2]["text"]==b and a[0][0]["text"]==".":
        a[0][0].config(text=b,state=DISABLED)
        return 1
        
    elif (a[1][0]["text"]==a[1][1]["text"]==b and a[1][2]["text"]=="."):
        a[1][2].config(text=b,state=DISABLED)
        return 1
    elif a[1][0]["text"]==a[1][2]["text"]==b and a[1][1]["text"]==".":
        a[1][1].config(text=b,state=DISABLED)
        return 1
    elif a[1][1]["text"]==a[1][2]["text"]==b and a[1][0]["text"]==".":
        a[1][0].config(text=b,state=DISABLED)
        return 1
        
    elif (a[2][0]["text"]==a[2][1]["text"]==b and a[2][2]["text"]=="."):
        a[2][2].config(text=b,state=DISABLED)
        return 1
    elif a[2][0]["text"]==a[2][2]["text"]==b and a[2][1]["text"]==".":
        a[2][1].config(text=b,state=DISABLED)
        return 1
    elif a[2][1]["text"]==a[2][2]["text"]==b and a[2][0]["text"]==".":
        a[2][0].config(text=b,state=DISABLED)
        return 1
        
    elif (a[0][2]["text"]==a[1][1]["text"]==b and a[2][0]["text"]=="."):
        a[2][0].config(text=b,state=DISABLED)
        return 1
    elif a[0][2]["text"]==a[2][0]["text"]==b and a[1][1]["text"]==".":
        a[1][1].config(text=b,state=DISABLED)
        return 1
    elif a[1][1]["text"]==a[2][0]["text"]==b and a[0][2]["text"]==".":
        a[0][2].config(text=b,state=DISABLED)
        return 1
        
    elif (a[0][1]["text"]==a[1][1]["text"]==b and a[2][1]["text"]=="."):
        a[2][1].config(text=b,state=DISABLED)
        return 1
    elif a[0][1]["text"]==a[2][1]["text"]==b and a[1][1]["text"]==".":
        a[1][1].config(text=b,state=DISABLED)
        return 1
    elif a[1][1]["text"]==a[2][1]["text"]==b and a[0][1]["text"]==".":
        a[0][1].config(text=b,state=DISABLED)
        return 1
        
    elif (a[0][2]["text"]==a[1][2]["text"]==b and a[2][2]["text"]=="."):
        a[2][2].config(text=b,state=DISABLED)
        return 1
    elif a[0][2]["text"]==a[2][2]["text"]==b and a[1][2]["text"]==".":
        a[1][2].config(text=b,state=DISABLED)
        return 1
    elif a[1][2]["text"]==a[2][2]["text"]==b and a[0][2]["text"]==".":
        a[0][2].config(text=b,state=DISABLED)
        return 1
    return 0

def foresight(b):
    if a[0][0]["text"]==a[0][1]["text"]=="." and a[0][2]["text"]==b:
        a[0][0].config(text=b,state=DISABLED)
        return 1
    elif a[0][0]["text"]==a[0][2]["text"]=="." and a[0][1]["text"]==b:
        a[0][0].config(text=b,state=DISABLED)
        return 1
    elif a[0][1]["text"]==a[0][2]["text"]=="." and a[0][0]["text"]==b:
        a[0][1].config(text=b,state=DISABLED)
        return 1

    elif (a[0][0]["text"]==a[1][0]["text"]=="." and a[2][0]["text"]==b):
        a[0][0].config(text=b,state=DISABLED)
        return 1
    elif a[0][0]["text"]==a[2][0]["text"]=="." and a[1][0]["text"]==b:
        a[0][0].config(text=b,state=DISABLED)
        return 1
    elif a[1][0]["text"]==a[2][0]["text"]=="." and a[0][0]["text"]==b:
        a[1][0].config(text=b,state=DISABLED)
        return 1
        
    elif (a[0][0]["text"]==a[1][1]["text"]=="." and a[2][2]["text"]==b):
        a[0][0].config(text=b,state=DISABLED)
        return 1
    elif a[0][0]["text"]==a[2][2]["text"]=="." and a[1][1]["text"]==b:
        a[0][0].config(text=b,state=DISABLED)
        return 1
    elif a[1][1]["text"]==a[2][2]["text"]=="." and a[0][0]["text"]==b:
        a[1][0].config(text=b,state=DISABLED)
        return 1
        
    elif (a[1][0]["text"]==a[1][1]["text"]=="." and a[1][2]["text"]==b):
        a[1][0].config(text=b,state=DISABLED)
        return 1
    elif a[1][0]["text"]==a[1][2]["text"]=="." and a[1][1]["text"]==b:
        a[1][0].config(text=b,state=DISABLED)
        return 1
    elif a[1][1]["text"]==a[1][2]["text"]=="." and a[1][0]["text"]==b:
        a[1][1].config(text=b,state=DISABLED)
        return 1
        
    elif (a[2][0]["text"]==a[2][1]["text"]=="." and a[2][2]["text"]==b):
        a[2][0].config(text=b,state=DISABLED)
        return 1
    elif a[2][0]["text"]==a[2][2]["text"]=="." and a[2][1]["text"]==b:
        a[2][0].config(text=b,state=DISABLED)
        return 1
    elif a[2][1]["text"]==a[2][2]["text"]=="." and a[2][0]["text"]==b:
        a[2][1].config(text=b,state=DISABLED)
        return 1
        
    elif (a[0][2]["text"]==a[1][1]["text"]=="." and a[2][0]["text"]==b):
        a[0][2].config(text=b,state=DISABLED)
        return 1
    elif a[0][2]["text"]==a[2][0]["text"]=="." and a[1][1]["text"]==b:
        a[0][2].config(text=b,state=DISABLED)
        return 1
    elif a[1][1]["text"]==a[2][0]["text"]=="." and a[0][2]["text"]==b:
        a[1][1].config(text=b,state=DISABLED)
        return 1
        
    elif (a[0][1]["text"]==a[1][1]["text"]=="." and a[2][1]["text"]==b):
        a[0][1].config(text=b,state=DISABLED)
        return 1
    elif a[0][1]["text"]==a[2][1]["text"]=="." and a[1][1]["text"]==b:
        a[0][1].config(text=b,state=DISABLED)
        return 1
    elif a[1][1]["text"]==a[2][1]["text"]=="." and a[0][1]["text"]==b:
        a[1][1].config(text=b,state=DISABLED)
        return 1
        
    elif (a[0][2]["text"]==a[1][2]["text"]=="." and a[2][2]["text"]==b):
        a[0][2].config(text=b,state=DISABLED)
        return 1
    elif a[0][2]["text"]==a[2][2]["text"]=="." and a[1][2]["text"]==b:
        a[0][2].config(text=b,state=DISABLED)
        return 1
    elif a[1][2]["text"]==a[2][2]["text"]=="." and a[0][2]["text"]==b:
        a[1][2].config(text=b,state=DISABLED)
        return 1
    return 0

def blockMove(b):
    if a[0][0]["text"]==a[0][1]["text"]!="." and a[0][2]["text"]==".":
        a[0][2].config(text=b,state=DISABLED)
        return 1
    elif a[0][0]["text"]==a[0][2]["text"]!="." and a[0][1]["text"]==".":
        a[0][1].config(text=b,state=DISABLED)
        return 1
    elif a[0][1]["text"]==a[0][2]["text"]!="." and a[0][0]["text"]==".":
        a[0][0].config(text=b,state=DISABLED)
        return 1

    elif (a[0][0]["text"]==a[1][0]["text"]!="." and a[2][0]["text"]=="."):
        a[2][0].config(text=b,state=DISABLED)
        return 1
    elif a[0][0]["text"]==a[2][0]["text"]!="." and a[1][0]["text"]==".":
        a[1][0].config(text=b,state=DISABLED)
        return 1
    elif a[1][0]["text"]==a[2][0]["text"]!="." and a[0][0]["text"]==".":
        a[0][0].config(text=b,state=DISABLED)
        return 1
        
    elif (a[0][0]["text"]==a[1][1]["text"]!="." and a[2][2]["text"]=="."):
        a[2][2].config(text=b,state=DISABLED)
        return 1
    elif a[0][0]["text"]==a[2][2]["text"]!="." and a[1][1]["text"]==".":
        a[1][1].config(text=b,state=DISABLED)
        return 1
    elif a[1][1]["text"]==a[2][2]["text"]!="." and a[0][0]["text"]==".":
        a[0][0].config(text=b,state=DISABLED)
        return 1
        
    elif (a[1][0]["text"]==a[1][1]["text"]!="." and a[1][2]["text"]=="."):
        a[1][2].config(text=b,state=DISABLED)
        return 1
    elif a[1][0]["text"]==a[1][2]["text"]!="." and a[1][1]["text"]==".":
        a[1][1].config(text=b,state=DISABLED)
        return 1
    elif a[1][1]["text"]==a[1][2]["text"]!="." and a[1][0]["text"]==".":
        a[1][0].config(text=b,state=DISABLED)
        return 1
        
    elif (a[2][0]["text"]==a[2][1]["text"]!="." and a[2][2]["text"]=="."):
        a[2][2].config(text=b,state=DISABLED)
        return 1
    elif a[2][0]["text"]==a[2][2]["text"]!="." and a[2][1]["text"]==".":
        a[2][1].config(text=b,state=DISABLED)
        return 1
    elif a[2][1]["text"]==a[2][2]["text"]!="." and a[2][0]["text"]==".":
        a[2][0].config(text=b,state=DISABLED)
        return 1
        
    elif (a[0][2]["text"]==a[1][1]["text"]!="." and a[2][0]["text"]=="."):
        a[2][0].config(text=b,state=DISABLED)
        return 1
    elif a[0][2]["text"]==a[2][0]["text"]!="." and a[1][1]["text"]==".":
        a[1][1].config(text=b,state=DISABLED)
        return 1
    elif a[1][1]["text"]==a[2][0]["text"]!="." and a[0][2]["text"]==".":
        a[0][2].config(text=b,state=DISABLED)
        return 1
        
    elif (a[0][1]["text"]==a[1][1]["text"]!="." and a[2][1]["text"]=="."):
        a[2][1].config(text=b,state=DISABLED)
        return 1
    elif a[0][1]["text"]==a[2][1]["text"]!="." and a[1][1]["text"]==".":
        a[1][1].config(text=b,state=DISABLED)
        return 1
    elif a[1][1]["text"]==a[2][1]["text"]!="." and a[0][1]["text"]==".":
        a[0][1].config(text=b,state=DISABLED)
        return 1
        
    elif (a[0][2]["text"]==a[1][2]["text"]!="." and a[2][2]["text"]=="."):
        a[2][2].config(text=b,state=DISABLED)
        return 1
    elif a[0][2]["text"]==a[2][2]["text"]!="." and a[1][2]["text"]==".":
        a[1][2].config(text=b,state=DISABLED)
        return 1
    elif a[1][2]["text"]==a[2][2]["text"]!="." and a[0][2]["text"]==".":
        a[0][2].config(text=b,state=DISABLED)
        return 1
    return 0

def randomMove(b):
    while(True):
        row=random.randint(0,2)
        column=random.randint(0,2)
        if(a[row][column]["text"]=="."):
            a[row][column].config(text=b,state=DISABLED)
            break

def checkWinCondition():
    global player
    if(a[0][0]["text"]==a[0][1]["text"]==a[0][2]["text"]!="."):
        a[0][0].config(bg="green")
        a[0][1].config(bg="green")
        a[0][2].config(bg="green")
        disableButtons()
        if a[0][0]["text"]==player:
            label.config(text="Game over.\nPlayer wins!")
        else:
            label.config(text="Game over.\nComputer wins!")
        return 0
    elif (a[0][0]["text"]==a[1][0]["text"]==a[2][0]["text"]!="."):
        a[0][0].config(bg="green")
        a[1][0].config(bg="green")
        a[2][0].config(bg="green")
        disableButtons()
        if a[0][0]["text"]==player:
            label.config(text="Game over.\nPlayer wins!")
        else:
            label.config(text="Game over.\nComputer wins!")
        
        return 0
    elif (a[0][0]["text"]==a[1][1]["text"]==a[2][2]["text"]!="."):
        a[0][0].config(bg="green")
        a[1][1].config(bg="green")
        a[2][2].config(bg="green")
        disableButtons()
        if a[0][0]["text"]==player:
            label.config(text="Game over.\nPlayer wins!")
        else:
            label.config(text="Game over.\nComputer wins!")
        
        return 0
    elif (a[1][0]["text"]==a[1][1]["text"]==a[1][2]["text"]!="."):
        a[1][0].config(bg="green")
        a[1][1].config(bg="green")
        a[1][2].config(bg="green")
        disableButtons()
        if a[1][0]["text"]==player:
            label.config(text="Game over.\nPlayer wins!")
        else:
            label.config(text="Game over.\nComputer wins!")
        
        return 0
    elif (a[2][0]["text"]==a[2][1]["text"]==a[2][2]["text"]!="."):
        a[2][0].config(bg="green")
        a[2][1].config(bg="green")
        a[2][2].config(bg="green")
        disableButtons()
        if a[2][0]["text"]==player:
            label.config(text="Game over.\nPlayer wins!")
        else:
            label.config(text="Game over.\nComputer wins!")
        
        return 0
    elif (a[0][2]["text"]==a[1][1]["text"]==a[2][0]["text"]!="."):
        a[0][2].config(bg="green")
        a[1][1].config(bg="green")
        a[2][0].config(bg="green")
        disableButtons()
        if a[0][2]["text"]==player:
            label.config(text="Game over.\nPlayer wins!")
        else:
            label.config(text="Game over.\nComputer wins!")
        
        return 0
    elif (a[0][1]["text"]==a[1][1]["text"]==a[2][1]["text"]!="."):
        a[0][1].config(bg="green")
        a[1][1].config(bg="green")
        a[2][1].config(bg="green")
        disableButtons()
        if a[0][1]["text"]==player:
            label.config(text="Game over.\nPlayer wins!")
        else:
            label.config(text="Game over.\nComputer wins!")
        
        return 0
    elif (a[0][2]["text"]==a[1][2]["text"]==a[2][2]["text"]!="."):
        a[2][2].config(bg="green")
        a[0][2].config(bg="green")
        a[1][2].config(bg="green")
        disableButtons()
        if a[0][2]["text"]==player:
            label.config(text="Game over.\nPlayer wins!")
        else:
            label.config(text="Game over.\nComputer wins!")
        
        return 0
    return 1
        
def toss():
    d=random.randint(0,1)
    if(d==0):
        return "O"
    else:
        return "X"

def disableButtons():
    for i in range(3):
        for j in range(3):
            a[i][j].config(state=DISABLED)

def play():
    global player
    global b
    player=toss()
    if player=="X":
        b="O"
    else:
        b="X"
    boardLayout()
                   
a= [[0,0,0],
    [0,0,0],
    [0,0,0]]

window = Tk()
window.title("Single Player")
window.geometry("250x260")


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