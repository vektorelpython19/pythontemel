import requests
from bs4 import BeautifulSoup
sayfa = requests.get("https://raw.githubusercontent.com/vektorelpython19/pythontemel/master/Proje/Hande/Ornek.html")
soup = BeautifulSoup(sayfa.content,'html.parser')
# print(sayfa.content)
# print(soup.prettify())
# print(list(soup.children))

liste = [type(item) for item in list(soup.children)]
print(liste)
