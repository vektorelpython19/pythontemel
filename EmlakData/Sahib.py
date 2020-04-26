

# def VeriCek(il,ilce,adim):
import requests
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
url = f'https://www.sahibinden.com/satilik-daire/ankara-cankaya?pagingOffset=0'
sayfa = requests.get(url, timeout=300,headers=HEADERS)
from bs4 import BeautifulSoup
soup = BeautifulSoup(sayfa.content,"html.parser")
# liste = soup.findAll("div",class_="result-text")

# print(list(liste)[0].span)
for item in soup.div.find_all_next("span"):
    print(item)

#     liste2 = soup.findAll("td",class_="searchResultsAttributeValue")
#     liste3 = soup.findAll("td",class_="searchResultsPriceValue")
#     liste4 = soup.findAll("td",class_="searchResultsDateValue")
#     liste5 = soup.findAll("td",class_="searchResultsLocationValue")
#     listeOda = []
#     listem2 = []
#     for i in range(len(liste2)):
#         if i % 2==0:
#             listem2.append(liste2[i])
#         else:
#             listeOda.append(liste2[i])
#     for i in range(len(liste3)):
#         m2 = listem2[i].text.replace("\n"," ").strip()
#         oda = listeOda[i].text.replace("\n"," ").strip()
#         fiyat = liste3[i].text.replace("\n"," ").strip()
#         tarih = liste4[i].text.replace("\n"," ").strip()
#         lokasyon = liste5[i].text.replace("\n","\\").replace(" ","")
#         print(f"{m2};{oda};{fiyat};{tarih},{lokasyon}")
#     print(len(liste2),len(liste3))


# for i in range(5):
#     VeriCek("ankara","cankaya",i*20)

# for item in liste2:
#     odaSay = item.findAll("td",class_="searchResultsAttributeValue")

#     print(odaSay.text)