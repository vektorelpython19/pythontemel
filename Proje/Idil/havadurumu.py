# https://www.mgm.gov.tr/?il=Ankara&ilce=Cankaya
import requests
from bs4 import  BeautifulSoup
param = "ankara"
sayfa = requests.get(f"http://www.{param}.mgm.gov.tr/tahmin-tum-merkezler.aspx")
soup = BeautifulSoup(sayfa.content,'html.parser')

tarih = soup.findAll("th",class_="th")

# for i in range(1,len(tarih)):
#     print(tarih[i].get_text())
#     merkez = soup.findAll("th",class_="alt_th")
#     for j in range(1,len(merkez)):
#         print(merkez[j].get_text())

print(tarih[1].get_text())
merkez = soup.findAll("th",class_="alt_th")
print(merkez[0].get_text())