from tkinter import *
foablak = Tk()
def kerulet():
    a = int(elso.get())
    b = int(masodik.get())
    c = int(harmadik.get())
    d = int(negyedik.get())
    e = a+b+c+d
    otodik.delete(0, END)
    otodik.insert(0, ''+str(e)+'cm')
elsomezo=Label(foablak, text='a')
elsomezo.grid()
elso=Entry(foablak)
elso.grid()
masodikmezo=Label(foablak, text='b')
masodikmezo.grid()
masodik=Entry(foablak)
masodik.grid()
harmadikmezo=Label(foablak, text='c')
harmadikmezo.grid()
harmadik=Entry(foablak)
harmadik.grid()
negyedikmezo=Label(foablak, text='d')
negyedikmezo.grid()
negyedik=Entry(foablak)
negyedik.grid()
gomb=Button(foablak, text='Kiszámít', command=kerulet)
gomb.grid()
eredmeny=Label(foablak, text='Kerület')
eredmeny.grid()
otodik=Entry(foablak)
otodik.grid()
foablak.mainloop()
