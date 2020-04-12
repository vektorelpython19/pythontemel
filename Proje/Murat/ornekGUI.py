from tkinter import *
pencere = Tk()
pencere.geometry("400x400+300+300")

etiket1 = Label(pencere,text="Kullanıcı Adı: ",width=40)
etiket1.grid(column=0,row=0)
txtUser = Entry(pencere,width=50)
txtUser.grid(column=1,row=0)

etiket2 = Label(pencere,text="Şifre: ",width=40)
etiket2.grid(column=0,row=1)
txtPass = Entry(pencere,show="*",width=50)
txtPass.grid(column=1,row=1)

def FonkGiris():
    if txtUser.get() and txtPass.get():
        if txtUser.get() =="Ediz"and txt.Pass.get() =="1234":
            print("Başarılı")
        else:
            print("Giriş Başarısız")

def Temizle():
    pass

dugme1 = Button(pencere,text ="Giriş Yap",width=30,command=FonkGiris)
dugme1.grid(column=0,row=2)
dugme2 = Button(pencere,text="Temizle",width=30,command=Temizle)
dugme2.grid(column=1,row=2)

pencere.mainloop()
    

