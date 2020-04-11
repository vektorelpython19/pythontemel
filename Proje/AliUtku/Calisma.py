import sqlite3 as sql

#db = sql.connect("/Users/yekta/PycharmProjects/pythontemel/Proje/IK.sqlite")
#cur = db.cursor()
#perId = int(input("Personel Id Giriniz : "))
#sorgu = f""" select adi,soyadi,email from personeller where personel_id = {perId}"""
#cur.execute(sorgu)
#liste = cur.fetchall()
#for k1,k2,k3 in liste:
#    print(k1,k2,k3)

class TelefonDefter:
    def __init__(self):
        self.db = sql.connect("/Users/yekta/PycharmProjects/pythontemel/Proje/IK.sqlite")
        self.cur = self.db.cursor()

    def Ekleme(self):
        try :
            adi = input("Adi Giriniz : ")
            soyadi = input("Soyadi Giriniz : ")
            tel_no = input("Telefon Numarasin Giriniz : ")
            sorgu = f"""INSERT INTO telefonlar (adi,soyadi,tel_no) VALUES ('{adi}','{soyadi}','{tel_no}')"""
            self.cur.execute(sorgu)
            self.db.commit()
            return True
        except Exception as Hata:
            print("Hata Mesaji : ",Hata)
            return False

    def Listele(self):
        try:
            sorgu = """SELECT tel_id,adi,soyadi,tel_no FROM telefonlar"""
            self.cur.execute(sorgu)
            for tel_id,adi,soyadi,tel_no in self.cur.fetchall():
                print(f"{tel_id}-{adi}-{soyadi}-{tel_no}")
        except Exception as Hata :
            print("Hata Mesaji : ",Hata)

    def __del__(self):
        self.cur.close()
        self.db.commit()
        self.db.close()

telefonDefter = TelefonDefter()
telefonDefter.Listele()
telefonDefter.Ekleme()
telefonDefter.Listele()