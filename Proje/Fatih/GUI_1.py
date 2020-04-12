from tkinter import *

pencere = Tk()
pencere.geometry("640x480+200+300")
etiket = Label(pencere,text="Pythondaki İlk Arayüz Elemanım")
etiket.grid(column=0,row=0)
def tiklandi():
    etiket["text"] = "Butona Tıklandı"
dugme = Button(pencere,text="Tıkla",command=tiklandi,width=20)
dugme.grid(column=1,row=0)

pencere.mainloop()

    
        








    