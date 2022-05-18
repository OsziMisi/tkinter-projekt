from tkinter import *
from tkinter import messagebox
import math
import turtle

foablak = Tk()
foablak.title("Síkidomok kerülete és területe ")
foablak.minsize(width = 500, height=150)

def terület():
        def szamit():
            a=eval(mezo1.get())
            b=eval(mezo2.get())
            felszin=a*b if a and b !=0 else "Az adat nem lehet 0!"
            mezo3.delete(0,END)
            mezo3.insert(0, str(felszin))
        
        abl3=Toplevel(foablak)
        abl3.title("Téglalap területe")
        abl3.minsize(width=100, height=100)
        szoveg1=Label(abl3, text="a:")
        szoveg2=Label(abl3, text="b:")
        szoveg3=Label(abl3, text="Eredmény:")
        gomb1=Button(abl3, text="Kiszámol", command=szamit)
        mezo1=Entry(abl3)
        mezo2=Entry(abl3)
        mezo3=Entry(abl3)
        szoveg1.grid(row=1)
        szoveg2.grid(row=2)
        szoveg3.grid(row=5)
        gomb1.grid(row=4, column=2, sticky=W)
        mezo1.grid(row=1, column=2, sticky=W)
        mezo2.grid(row=2, column=2, sticky=W)
        mezo3.grid(row=5, column=2, sticky=W)
        gomb2=Button(abl3, text="Kilépés", command=abl3.destroy)
        gomb2.grid(row=6, column=4, sticky=W)
        abl3.mainloop()

def kerület():
        def szamit():
            a=eval(mezo1.get()) 
            b=eval(mezo2.get())
            terfogat=2*(a+b) if a and b !=0 else "Hiba, az egyik adat 0!"
            mezo3.delete(0,END)
            mezo3.insert(0,str(terfogat))

        abl3=Toplevel(foablak)
        abl3.title("Téglalap kerülete")
        abl3.minsize(width=100, height=100)
        szoveg1=Label(abl3, text="a:")
        szoveg2=Label(abl3, text="b:")
        szoveg3=Label(abl3, text="Eredmény:")
        gomb1=Button(abl3, text="Kiszámol", command=szamit)
        mezo1=Entry(abl3)
        mezo2=Entry(abl3)
        mezo3=Entry(abl3)
        szoveg1.grid(row=1)
        szoveg2.grid(row=2)
        szoveg3.grid(row=5)
        gomb1.grid(row=4, column=2, sticky=W)
        mezo1.grid(row=1, column=2, sticky=W)
        mezo2.grid(row=2, column=2, sticky=W)
        mezo3.grid(row=5, column=2, sticky=W)
        gomb2=Button(abl3, text="Kilépés", command=abl3.destroy)
        gomb2.grid(row=6, column=4, sticky=W)
        abl3.mainloop()



menusor=Frame(foablak)
menusor.pack(side=TOP, fill=X)

menu1=Menubutton(menusor, text="Téglalap", underline=0)
menu1.pack(side=LEFT)
teglalap=Menu(menu1)
teglalap.add_command(label="Terület", command=terület, underline=0)
teglalap.add_command(label="Kerület", command=kerület, underline=0)
menu1.config(menu=teglalap)

#Turtle szekció
t = turtle.Turtle()
t.forward(150) #Forward turtle by 150 units
t.left(90) #Turn turtle by 90 degree
t.forward(80) #Forward turtle by 80 units
t.left(90) #Turn turtle by 90 degree
t.forward(150) #Forward turtle by 150 units
t.left(90) #Turn turtle by 90 degree
t.forward(80) #Forward turtle by 80 units
t.left(90) #Turn turtle by 90 degree
#Turtle szekció
foablak.mainloop()