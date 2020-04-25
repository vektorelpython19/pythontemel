import requests
from bs4 import BeautifulSoup
sayfa = requests.get("https://raw.githubusercontent.com/vektorelpython19/pythontemel/master/Proje/Hande/Ornek.html")
soup = BeautifulSoup(sayfa.content,'html.parser')
print(soup.find('div',class_="ikinciDiv").get_text())
# print(sayfa.content) # ED%C4%B0Z
# print(soup.prettify())
# print(list(soup.children))

# liste = [type(item) for item in list(soup.children)]

# html = list(soup.children)[0]
# body = list(html.children)[3]
# p=list(body.children)[1]

# print(p.get_text())
