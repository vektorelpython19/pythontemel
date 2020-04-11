import sqlite3 as sql
db = sql.connect(r"DB\IK.sqlite")
cur = db.cursor()
sorgu = """
SELECT * FROM isler ORDER BY is_id desc """
cur.execute(sorgu)
liste = cur.fetchall()
print(*liste,sep="\n")
