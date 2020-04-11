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


    def __del__(self):
        self.cur.close()
        self.db.commit()
        self.db.close()