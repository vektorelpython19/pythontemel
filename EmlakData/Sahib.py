import requests
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
url = 'https://www.sahibinden.com/satilik-daire/ankara-cankaya?pagingOffset=100'
sayfa = requests.get(url, timeout=300,headers=HEADERS)
from bs4 import BeautifulSoup
soup = BeautifulSoup(sayfa.content,"html.parser")
i = 0
# for item in list(soup.children):
#     print(i,type(item))
#     i += 1 
# eleman = list(soup.children)[32]

# for item in eleman:
#     liste = item.find(class_="searchResultsTitleValue leafContent")
#     print(liste)
# -------------------------
# liste = soup.findAll("td",class_="searchResultsTitleValue leafContent")
liste2 = soup.findAll("td",class_="searchResultsAttributeValue")
liste3 = soup.findAll("td",class_="searchResultsPriceValue")
liste4 = soup.findAll("td",class_="searchResultsDateValue")
liste5 = soup.findAll("td",class_="searchResultsLocationValue")
for i in range(len(liste3)):
    fiyat = liste3[i].text.replace("\n"," ").strip()
    tarih = liste4[i].text.replace("\n"," ").strip()
    lokasyon = liste5[i].text.replace("\n","\\").replace("  ","")
    print(f"{fiyat};{tarih},{lokasyon}")



# for item in liste2:
#     odaSay = item.findAll("td",class_="searchResultsAttributeValue")

#     print(odaSay.text)