import sqlite3 as sql

class DataEmlak:
    def __init__(self):
        self.db = sql.connect(r"Proje\Idil\Emlak\DB\Emlak.db")
        self.cur = self.db.cursor()
        # self.ilOlustur()
        # self.ilceOlustur()

    def ilOlustur(self):
        sorgu = """
        CREATE TABLE IF NOT EXISTS  ST_ILLER (
            IL_ID  INTEGER      PRIMARY KEY
                                NOT NULL,
            IL_ADI VARCHAR (30) NOT NULL
        );
        """
        self.cur.execute(sorgu)

    def ilceOlustur(self):
        sorgu = """
        CREATE TABLE IF NOT EXISTS ST_ILCELER (
            ST_ILCE_ID  INTEGER      PRIMARY KEY
                                    NOT NULL,
            ST_ILCE_ADI VARCHAR (40) NOT NULL,
            ST_IL       INTEGER      NOT NULL
                                    CONSTRAINT FK_STIL_STILCE REFERENCES ST_ILLER (IL_ID) 
        )""" 
        self.cur.execute(sorgu)

    def ilListele(self):
        sorgu = """ SELECT IL_ID,IL_ADI FROM ST_ILLER """
        return self.cur.execute(sorgu).fetchall()
    
    def ilceListele(self,ID):
        sorgu = f"""SELECT 
        ST_ILCE_ID,ST_ILCE_ADI 
        FROM ST_ILCELER WHERE ST_IL = {ID}"""
        return self.cur.execute(sorgu).fetchall()

