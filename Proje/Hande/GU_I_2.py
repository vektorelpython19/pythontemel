    # -*- coding: utf-8 -*-
    """
    Created on Sun Apr 12 12:03:16 2020
    
    @author: LENOVO
    """
    
    
    from tkinter import *
    pencere=Tk()
    pencere.geometry("600x600+300+300")
    
    etiket1 = Label(pencere,text="Kullanıcı Adı:",width=40)
    etiket1.grid(column=0,row=0)
    txtUser=Entry(pencere,width=50)
    txtUser.grid(column=1,row=0)
    
    etiket2 = Label(pencere,text="Şifre:",width=50)
    etiket1.grid(column=0,row=0)
    txtPass=Entry(pencere,show="*",width=50)
    txtPass.grid(column=1,row=1)
    
    def FonkGiris():
        if txtUser.get() and txtPass.get():
            if txtUser.get()=="Hande" and txtPass.get()=="123":
                sonuc["text"]="Giriş Başarılı"
            else:
                sonuc["text"]="Giriş Başarılı"
                
    def Temizle():
        txtUser.delete(0,END)
        txtUser.insert(0,"")
        txtPass.delete(0,END)
        txtPass.insert(0,"")
    
    dugme1=Button(pencere,text="Giriş Yap",width=30,command=FonkGiris)
    dugme1.grid(column=0,row=2)
    dugme2=Button(pencere,text="Temizle",width=30,command=Temizle)
    dugme2.grid(column=1,row=2)
    
    sonuc=Label(pencere,text="",width=40)
    sonuc.grid(column=0,row=3)
    
    pencere.mainloop()