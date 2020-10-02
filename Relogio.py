from tkinter import *
from time import strftime

def tic():
    rel["text"] = strftime("%H:%M:%S")
    rel["font"] = "Helvetico 120 bold"

def tac():
    tic()
    rel.after(1000,tac)

main = Tk()
rel = Label(main)
rel.pack()
tac()
main.mainloop()