from tkinter import *

pencere = Tk()
pencere.geometry("640x480+200+300")
etiket = Label(pencere, text="Pythondaki ilk arayuz elemanim")
etiket.grid(column=0, row=0)


def tiklandi():
    etiket["text"] = "Butona Tiklandi"


dugme = Button(pencere, text="Tikla", command=tiklandi, width=20)

def tiklandi2():
    yazi = txt.get()
    etiket.configure(text=yazi)


txt = Entry(pencere,width=20)
txt.grid(column=0,row=1)
dugme = Button(pencere, text="Aktar", command=tiklandi2)
dugme.grid(column=1,row=1)

pencere.mainloop()
