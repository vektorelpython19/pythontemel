import requests
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
url = 'https://www.sahibinden.com/satilik-daire/ankara-cankaya'
sayfa = requests.get(url, timeout=300,headers=HEADERS)
from bs4 import BeautifulSoup
soup = BeautifulSoup(sayfa.content,"html.parser")
i = 0
for item in list(soup.children):
    print(i,type(item))
    i += 1 
eleman = list(soup.children)[32]
print(eleman.prettify())
# for item in eleman:
#     liste = item.find(class_="searchResultsTitleValue leafContent")
#     print(liste)
#-------------------------
# liste = soup.findAll("td",class_="searchResultsTitleValue leafContent")
# liste2 = soup.findAll("td",class_="searchResultsAttributeValue")
# for item in liste:
#     odaSay = list(item.findAll("td",class_="searchResultsAttributeValue"))[0]

#     print(odaSay.text)