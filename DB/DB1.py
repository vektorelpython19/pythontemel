import sqlite3 as sql
db = sql.connect(r"IK.sqlite")
cur = db.cursor()
sorgu = """
SELECT is_unvan FROM isler ORDER BY is_id desc """
cur.execute(sorgu)
liste = cur.fetchall()
print(*liste,sep="\n")
print(liste)
print(*liste,sep="\n")
