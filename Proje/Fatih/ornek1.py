import sqlite3 as sql
#select * from personeller limit 5
#db = sql.connect("Proje\IK.sqlite")
#cur = db.cursor()
#perId = int(input("Personel ID Giriniz:"))
#sorgu = f""" select adi,soyadi,email from personeller where personel_id = {perId}"""
#cur.execute(sorgu)
#liste = cur.fetchall()
#for k1,k2,k3 in liste:
#    print(k1,k2,k3)

class TelefonDefter:
    def __init__(self):
        self.db = sql.connect("Proje\IK.sqlite")
        self.cur = self.db.cursor()

    def girisAl(self):
        adi=input("Adı Giriniz:")
        soyadi=input("Soyadı Giriniz:")
        tel_no=input("Telefon Numarası Giriniz:")
        return adi,soyadi,tel_no


    def Ekleme(self):
        try:
            adi=input("Adı Giriniz:")
            soyadi=input("Soyadı Giriniz:")
            tel_no=input("Telefon Numarası Giriniz:")
            sorgu = f"""
            INSERT INTO telefonlar (adi,soyadi,tel_no) VALUES ('{adi}','{soyadi}','{tel_no}')"""
            self.cur.execute(sorgu)
            self.db.commit()
            return True
        except Exception as hata:
            print("Hata Mesajı:",hata)
            return False
    def Listele(self):
        try:
            sorgu= """select tel_id,adi,soyadi,tel_no from telefonlar"""
            self.cur.execute(sorgu)
            for tel_id,adi,soyadi,tel_no in self.cur.fetchall():
                print(f"{tel_id} {adi} {soyadi} {tel_no}")
        except Exception as hata:
            print("Hata Mesajı:",hata)

    def __del__(self):
        self.cur.close()
        self.db.commit()
        self.db.close()
    
    def Guncelleme(self):
        try:
            tel_id=input("Sıra Numarası Giriniz:")
            adi=input("Adı Giriniz:")
            soyadi=input("Soyadı Giriniz:")
            tel_no=input("Telefon Numarası Giriniz:")
            self.cur.execute("UPDATE telefonlar SET adi='adi',soyadi='soyadi',tel_no='tel_no' WHERE tel_id=?",(tel_id,))
            self.db.commit()
            return True
        except Exception as hata:
            print("Hata Mesajı:",hata)
            return False

    def verisil(self):
        try:
            tel_id=input("Sıra Numarası Giriniz:")
            self.cur.execute("DELETE FROM telefonlar WHERE tel_id==?",(tel_id,))
            self.db.commit()
            print ("Başarıyla silindi.")
        except Exception as hata:
            print("Hata Mesajı:",hata)
            return False

telefonDefter = TelefonDefter()


print("""
***********MENÜ***********
1- Kişi Ekle
2- Listeyi Görüntüle
3- Listeyi Güncelle
4- Kayıt Sil
5- Programdan Çıkış

""")
while True:
    secim=input("Bir İşlem Giriniz:")
    if secim == "1":
        telefonDefter.Ekleme()
    elif secim == "2":
        telefonDefter.Listele()
    elif secim == "3":
        telefonDefter.Guncelleme()
    elif secim== "4":
        telefonDefter.verisil()
    elif secim== "5":
        print("Program Sonlandırıldı...")
    
    else:
        print("Geçerli Bir İşlem Kodu Girmediniz!!!")
    
        








    