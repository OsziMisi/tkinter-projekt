from tkinter import *
from tkinter import messagebox
import math


foablak = Tk()
foablak.title('Síkidomok kerülete és területe ')
foablak.minsize(width = 500, height=150)

a = PhotoImage(file = 'rombusz.jpg')
foablak.iconphoto(False, a)

def terület():
        def szamit():
            a=eval(mezo1.get())
            b=eval(mezo2.get())
            felszin=a*b if a and b !=0 else "Hibas kerlek ne irj be mast"
            mezo3.delete(0,END)
            mezo3.insert(0, str(felszin))

foablak.mainloop()

