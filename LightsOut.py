import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# print("Welcome to lights out.")

base = [[0,0,1,0,0],
        [1,0,1,0,1],
        [1,1,1,1,1],
        [1,0,1,0,1],
        [0,0,1,0,0]]

updated = base


window = Tk()

def checkComplete():
        count = 0
        for i in range(len(updated)):
                for ii in range(len(updated[i])):
                        if(updated[i][ii] == 1):
                                count += 1
        if(count == 0):
                messagebox.showinfo("Complete", "The runes all grow dark and sleek black. The face of the cube retracts, revealing a black coin with the head of a mare on it.\n\nSend me a pic of this window so I know it's done. ")

#TKinter
runeOff = ImageTk.PhotoImage(Image.open('images\Rune Off.jpg'))
runeOn = ImageTk.PhotoImage(Image.open('images\Rune On.jpg'))

window.configure(background = 'black')
window.title("Black Cube Puzzle")
imageBoard = [[Button for x in range(5)] for y in range(5)]

def switch(x, y):
        if(updated[x][y] == 1):
                updated[x][y] = 0
        elif(updated[x][y] == 0):
                updated[x][y] = 1

def switchAll(x,y):
        switch(x,y)
        update(x,y)
        if(x != 0):
                switch(x-1,y)
                update(x-1,y)
        if(x != 4):
                switch(x+1,y)
                update(x+1,y)
        if(y != 0):
                switch(x, y-1)
                update(x, y-1)
        if(y != 4):
                switch(x, y+1)
                update(x, y+1)
        checkComplete()

def setBoard():
        for i in range(len(base)):
                for ii in range(len(base[i])):
                        update(i,ii)

def updateBoard():
        for i in range(len(updated)):
                for ii in range(len(updated[i])):
                        update(i,ii)

def update(x, y):
        if (updated[x][y] == 1):
                Button(window, image=runeOn, command = lambda: switchAll(x, y)).grid(row=x, column=y)
        elif(updated[x][y] == 0):
                Button(window, image=runeOff, command = lambda: switchAll(x, y)).grid(row=x, column=y)

setBoard()
# Button(window, text = "Reset", command = lambda: resetBoard()).grid(row = 5, column = 2)
base = [[0,0,1,0,0],
        [1,0,1,0,1],
        [1,1,1,1,1],
        [1,0,1,0,1],
        [0,0,1,0,0]]

window.mainloop()

