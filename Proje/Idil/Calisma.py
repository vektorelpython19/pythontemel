import sqlite3 as sql
#select * from personeller LIMIT 5
#db = sql.connect(r"Proje\IK.sqlite")
#cur = db.cursor()
#perId = int(input("Personel ID giriniz:"))
#sorgu = f"""select adi,soyadi,email from personeller where personel_id= {perId}"""
#cur.execute(sorgu)
#liste = cur.fetchall()
#for k1,k2,k3 in liste:
#    print(k1,k2,k3)

class TelefonDefter:
    def __init__(self):
        self.db = sql.connect("Proje\IK.sqlite")
        self.cur = self.db.cursor()
    
    def Ekleme(self):
        try:
            adi = input("Adı Giriniz:")
            soyadi = input("Soyadı Giriniz:")
            tel_no = input("Telefon Numarası Giriniz:")
            sorgu = f"""INSERT 
            INTO telefonlar (adi,soyadi,tel_no) VALUES ('{adi}','{soyadi}','{tel_no}')"""
            self.cur.execute(sorgu)
            # commit onaylama
            # rollback gerialma
            self.db.commit()
            return True
        except Exception as hata:
            print("Hata Mesajı:",hata)
            return False
        
    def Listele(self):
        try:
            sorgu = """ SELECT tel_id,adi,soyadi,tel_no FROM telefonlar """
            self.cur.execute(sorgu)
            for tel_id,adi,soyadi,tel_no in self.cur.fetchall():
                print(f"{tel_id}-{adi} {soyadi} {tel_no}")
        except Exception as hata:
            print("Hata Mesajı:",hata)

    def __del__(self):
        self.cur.close()
        self.db.commit()
        self.db.close()
    
telefonDefter = TelefonDefter()
telefonDefter.Listele()
telefonDefter.Ekleme()
telefonDefter.Listele()

