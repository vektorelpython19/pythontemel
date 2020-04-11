import sqlite3 as sql
#select * from personeller LIMIT 5
db = sql.connect(r"Proje\IK.sqlite")
cur = db.cursor()
sorgu = """select adi,soyadi,email from personeller LIMIT 5"""
cur.execute(sorgu)
liste = cur.fetchall()
for k1,k2,k3 in liste:
    print(k1,k2,k3)