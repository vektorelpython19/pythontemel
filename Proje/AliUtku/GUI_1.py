from tkinter import *

pencere = Tk()
pencere.geometry("640x480+200+300")
etiket= Label(pencere,text="Pythondaki ilk arayüz elemanım")
etiket.grid(column=0,row=0)
def tiklandi():
    etiket["text"] = "Butona Tıkladı"
dugme = Button(pencere,text="Tıkla",command=tiklandi,width=20)
dugme.grid(column=1,row=0)

def tiklandi2():
    yazi = txt.get()
    etiket.configure(text=yazi)

txt = Entry(pencere,width=20)
txt.grid(column=0,row=1)

dugme2= Button(pencere,text="Aktar",command=tiklandi2)
dugme2.grid(column=1,row=1)


pencere.mainloop()