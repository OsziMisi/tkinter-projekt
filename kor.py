def kor():
    def szamitas():
        try:
            sugar = int(mezo1.get())
            if sugar == 0 or r < 0:
                showerror("Gaz van itt kerem főnök!", "Nem lehet nulla, vagy nullánál kisebb!")
            else:
                terulet = r*r*3.14
                eredmeny_mezo.configure(state=NORMAL)
                eredmeny_mezo.delete(0, END)
                eredmeny_mezo.insert(0, terulet)
                eredmeny_mezo.configure(state=DISABLED)