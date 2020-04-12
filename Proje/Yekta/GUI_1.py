from tkinter import *


pencere = Tk()
pencere.geometry("640x480+200+300")
etiket = Label(pencere,text="Pythondaki ilk arayuz elemanim")
etiket.grid(column=0,row=0)

def tiklandi():
    etiket["text"] = "Butona Tiklandi"

dugme = Button(pencere,text="Tikla",command=tiklandi)
dugme.grid(column=1,row=0)
pencere.mainloop()