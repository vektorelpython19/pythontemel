import sqlite3 as sql
#db = sql.connect(r"Proje\IK.sqlite")
#cur = db.cursor()
#perId = int(input("Personel ID giriniz:"))
#sorgu = f""" select adi,soyadi,email from personeller Where personel_id = {perId} """
#cur.execute(sorgu)
#liste = cur.fetchall()
#for k1,k2,k3 in liste:
#    print(k1,k2,k3)



class TelefonDefter:
    def__init__(self):
       self.db = sql.connect("Proje\IK.sqlite")
       self.cur = self.db.cursor()
    
    def Ekleme(self):
        adi= input("Adı Giriniz:")
        soyadi = input("Soyadi Giriniz:")
        tel_no = input("Telefon Numarası Giriniz:")
        sorgu = f"""
        INSERT INTO telefonlar (adi,soyadi,tel_no) VALUES ('{}','{}','{}')"""
        self.cur.execute(sorgu)
        self.db.commit()
        return True
    except Exception as hata:
        print("Hata Mesajı:",hata)
        return False



       def__del__(self):
          self.cur.close()
          self.db.commit()
          self.db.close() 