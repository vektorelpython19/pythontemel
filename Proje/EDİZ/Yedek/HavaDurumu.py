# https://www.mgm.gov.tr/?il=Ankara&ilce=Cankaya
import requests
from bs4 import  BeautifulSoup
param = "ankara"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
url = f"https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=Ankara&ilce=%C3%87ankaya"
sayfa = requests.get(url, timeout=300,headers=HEADERS)
soup = BeautifulSoup(sayfa.content,'html.parser')

liste = soup.find(class_="anlik-durum")
# print(liste)
for item in liste:
    print(item)

# tarih = soup.findAll("th",class_="th")

# for i in range(1,len(tarih)):
#     print(tarih[i].get_text())
#     merkez = soup.findAll("th",class_="alt_th")
#     for j in range(1,len(merkez)):
#         print(merkez[j].get_text())

# print(tarih[1].get_text())
# merkez = soup.findAll("th",class_="alt_th")
# print(merkez[0].get_text())