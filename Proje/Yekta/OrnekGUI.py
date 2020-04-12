from tkinter import *

pencere = Tk()
pencere.geometry("600x800+300+300")

etiket = Label(pencere, text="Kullanici Adi : ", width=40)
etiket.grid(column=0, row=0)

txtUser = Entry(pencere, width=50)
txtUser.grid(column=1, row=0)

etiket2 = Label(pencere, text="Sifre :", width=40)
etiket2.grid(column=0, row=1)
txtPass = Entry(pencere,show="*",width=50)
txtPass.grid(column=1, row=1)


def fonkGiris():
    if txtUser.get() and txtPass.get():
        if txtUser.get() == "Yekta" and txtPass.get() == "1234":
            print("Giris Basarili")
        else:
            print("Giris Basarisiz")


def temizle():
    pass


dugme1 = Button(pencere, text="Giris Yap", width=30, command=fonkGiris)
dugme1.grid(column=0, row=2)

dugme1 = Button(pencere, text="Temizle", width=30, command=temizle)
dugme1.grid(column=1, row=2)

pencere.mainloop()
