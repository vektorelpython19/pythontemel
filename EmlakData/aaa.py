import os 
import datetime
tarih = datetime.datetime.today()
il = "ankara"
ilce = "cankaya"
print(f"{il}_{ilce}_{tarih.day}_{tarih.month}_{tarih.year}.csv")
# os.makedirs("ankara/cankaya")