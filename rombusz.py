from tkinter import *
from tkinter import messagebox
import math
import tkinter as tk




foablak = tk.Tk()
foablak.minsize(width = 500, height=150)
foablak.title('Síkidomok kerülete és területe')
#foablak.tk.call('wm', 'iconphoto', foablak._w, tk.PhotoImage(file='C:\\Users\\oroszlanmihaly\\Documents\\GitHub\\tkinter-projekt\\rombusz.png'))


#területet ide
def terület():     
    def szamit():
        a=eval(mezo1.get())
        m=eval(mezo2.get())
        felszin=a*m if a and a!=0 else "Hibas kerlek ne irj be mast"
        mezo3.delete(0,END)
        mezo3.insert(0, str(felszin))

    ablak3=Toplevel(foablak)
    ablak3.title('Ez a rombusz területe')
    ablak3.minsize(width=400, height=100)
    szoveg1=Label(ablak3, text="Alap (cm)")
    szoveg2=Label(ablak3, text='Magasság (cm)')
    szoveg3=Label(ablak3, text="Eredmény: (cm2)")
    gomb1=Button(ablak3, text="Kiszámol", command=szamit)
    mezo1=Entry(ablak3)
    mezo2=Entry(ablak3)
    mezo3=Entry(ablak3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=5)
    gomb1.grid(row=3, column=2, sticky=W)
    mezo1.grid(row=1, column=2, sticky=W) #hibaas fos [javitani kell]
    mezo2.grid(row=2, column=2, sticky=W)
    mezo3.grid(row=5, column=2, sticky=W)
    gomb2=Button(ablak3, text="Kilépés", command=ablak3.destroy)
    gomb2.grid(row=6, column=4, sticky=W)
    ablak3.mainloop()



def kerület():
        def szamit():
            a=eval(mezo1.get()) 
            terfogat=2*(a+a+a+a) if a !=0 else "Hiba, az egyik adat 0!"
            mezo3.delete(0,END)
            mezo3.insert(0,str(terfogat))

        ablak3=Toplevel(foablak)
        ablak3.title("Téglalap kerülete")
        ablak3.minsize(width=400, height=200)
        szoveg1=Label(ablak3, text="a:")
        szoveg3=Label(ablak3, text="Eredmény:")
        gomb1=Button(ablak3, text="Kiszámol", command=szamit)
        mezo1=Entry(ablak3)
        mezo2=Entry(ablak3)
        mezo3=Entry(ablak3)
        szoveg1.grid(row=1)
        szoveg3.grid(row=2)
        szoveg3.grid(row=5)
        gomb1.grid(row=4, column=2, sticky=W)
        mezo1.grid(row=1, column=2, sticky=W)
        mezo2.grid(row=2, column=2, sticky=W)
        mezo3.grid(row=5, column=2, sticky=W)
        gomb2=Button(ablak3, text="Kilépés", command=ablak3.destroy)
        gomb2.grid(row=6, column=4, sticky=W)
        ablak3.mainloop()



menusor=Frame(foablak)
menusor.pack(side=TOP, fill=X)

menu1=Menubutton(menusor, text="Rombusz", underline=0)
menu1.pack(side=LEFT)
teglalap=Menu(menu1)
teglalap.add_command(label="Terület", command=terület, underline=0)
teglalap.add_command(label="Kerület", command=kerület, underline=0)
menu1.config(menu=teglalap)



foablak.mainloop()

