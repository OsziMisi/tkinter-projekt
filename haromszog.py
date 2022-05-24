from tkinter import *
from tkinter import messagebox
import math
import turtle

foablak = Tk()
foablak.title("A téglatest adatai")
foablak.minsize(width = 300, height=100)
menusor = Frame(foablak)
menusor.pack(side=TOP, fill=X)
menu7 = Menubutton(menusor, text="Háromszög", underline=0)
menu7.pack(side = LEFT)
teglatest=Menu(menu7)



#Turtle szekció
board = turtle.Turtle() 
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
turtle.done()
#Turtle szekció
foablak.mainloop()