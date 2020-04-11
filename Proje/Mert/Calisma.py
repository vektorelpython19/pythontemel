import sqlite3 as sql
# select * from personeller LIMIT 5
db = sql.connect("Proje\IK.sqlite")
cur = db.cursor()
perID = int(input("Personel ID giriniz: "))
sorgu = f"""select adi,soyadi,email from personeller Where personel_id = {perID}"""
cur.execute(sorgu)
liste = cur.fetchall()
for k1,k2,k3 in liste:
    print(k1,k2,k3)