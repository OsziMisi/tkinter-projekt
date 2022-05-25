from tkinter import *
from tkinter import messagebox
import math
import turtle


def kerulet():
    
    def szamit():
        hiba=mezo1.get()
        if len(hiba) == 0:
            messagebox.showerror('Error message box', "A mező üres")
        else:
            pass  
        hiba=int(hiba)

        a = eval(mezo1.get())
       #b = eval(mezo2.get())
       #c = eval(mezo3.get())
        kerulet = a*4
        mezo4.delete(0,END)
        mezo4.insert(0,str(kerulet))
    abl3=Tk()
    abl3.title("A Négyzet kerület")
    abl3.minsize(width=300, height=100)
    szoveg1 = Label(abl3, text="a")
   #szoveg2 = Label(abl3, text="b")
   #szoveg3 = Label(abl3, text="c")
    szoveg4 = Label(abl3, text="Eredmeny")
    gomb1 = Button(abl3, text ="Számítás", command=szamit)
    mezo1 = Entry(abl3)
   #mezo2 = Entry(abl3)
   #mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row=1)
   #szoveg2.grid(row=2)
   #szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2)
    mezo1.grid(row=1, column=2)
   #mezo2.grid(row=2, column=2)
   #mezo3.grid(row=3, column=2)
    mezo4.grid(row=5, column=2)
    abl3.mainloop()

    #Kerület vége
def terulet():
    
    def szamit():
        hiba=mezo1.get()
        if len(hiba) == 0:
            messagebox.showerror('Error message box', "üres a mező ")
        else:
            pass  
        hiba=int(hiba)

        a = eval(mezo1.get())
        #b = eval(mezo2.get())
        #c = eval(mezo3.get())
        terulet = a**2
        mezo4.delete(0,END)
        mezo4.insert(0,str(terulet))
    abl3=Tk()
    abl3.title("A Négyzet területe")
    abl3.minsize(width=300, height=100)
    szoveg1 = Label(abl3, text="a")
  # szoveg2 = Label(abl3, text="b")
  # szoveg3 = Label(abl3, text="c")
    szoveg4 = Label(abl3, text="Eredmeny")
    gomb1 = Button(abl3, text ="Számítás", command=szamit)
    mezo1 = Entry(abl3)
   #mezo2 = Entry(abl3)
   #mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row=1)
   #szoveg2.grid(row=2)
   #szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2)
    mezo1.grid(row=1, column=2)
   #mezo2.grid(row=2, column=2)
   #mezo3.grid(row=3, column=2)
    mezo4.grid(row=5, column=2)
    abl3.mainloop()



foablak = Tk()
foablak.title("A téglatest adatai")
foablak.minsize(width = 300, height=100)
menusor = Frame(foablak)
menusor.pack(side=TOP, fill=X)
menu7 = Menubutton(menusor, text="Négyzet", underline=0)
menu7.pack(side = LEFT)
teglatest=Menu(menu7)
teglatest.add_command(label="Kerület", command = kerulet, underline=0)
teglatest.add_command(label="Terület", command = terulet, underline=0)
menu7.config(menu = teglatest)
t = turtle.Turtle()

#Turtle szekció
t.forward(100) 
t.left(90) 
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
#Turtle szekció
foablak.mainloop()