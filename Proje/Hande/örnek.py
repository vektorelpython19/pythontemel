import requests
from bs4 import BeautifulSoup
sayfa=requests.get("https://raw.githubusercontent.com/vektorelpython19/pythontemel/master/Proje/Hande/Ornek.html")
soup=BeautifulSoup(sayfa.content,"html.parser")
print(soup.prettify())
print(list(soup.children))