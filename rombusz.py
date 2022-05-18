from tkinter import *
from tkinter import messagebox
import math
import tkinter as tk




foablak = tk.Tk()
foablak.title('Síkidomok kerülete és területe ')
foablak.minsize(width = 500, height=150)
foablak.tk.call('wm', 'iconphoto', foablak._w, tk.PhotoImage(file='C:\\Users\\oroszlanmihaly\\Documents\\GitHub\\tkinter-projekt\\rombusz.png'))



def terület():     
    def szamit():
        a=eval(mezo1.get())
        b=eval(mezo2.get())
        felszin=a*a*a*a if a and b !=0 else "Hibas kerlek ne irj be mast"
        mezo3.delete(0,END)
        mezo3.insert(0, str(felszin))

ablak3=Toplevel(foablak)
ablak3.title('Ez a rombusz kerülete és területe')
foablak.mainloop()

