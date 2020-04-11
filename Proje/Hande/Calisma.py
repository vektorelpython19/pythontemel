import sqlite3 as sql
db=sql.connet("Proje\IK.sqlite")
cur=db.cursor()
perId=int(input('Personel ID giriniz:'))
sorgu=f"select adi,soyadi,email from Where personel_id={perId}"
cur.execute(sorgu)
liste=cur.fetchall()
for k1,k2,k3 in liste:
  print(k1,k2,k3)
