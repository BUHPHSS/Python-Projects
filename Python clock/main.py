#Before running program, install the ds-digital font fron the link: - https://www.dafont.com/ds-digital.font

# Importing tkinter module
from tkinter import *
from tkinter.ttk import *

# Get system's time
from time import strftime

root = Tk()
root.title('Clock')

# Display time on label
def time():
    string = strftime('%I:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

# Font and background color
lbl = Label(root, font=('ds-digital', 80),
            background='black',
            foreground='cyan')

# Putting the clock in the middle
lbl.pack(anchor='center')
time()
mainloop()