import requests
from bs4 import BeautifulSoup
sayfa = requests.get("https://github.com/vektorelpython19/pythontemel/blob/master/Proje/AliUtku/Ornek.html")
soup = BeautifulSoup(sayfa.content,'html.parser')
#print(sayfa.content)
#print(soup.prettify())
#print(list(soup.children))

#liste = [type(item) for item in list(soup.children)]

#html = list(soup.children)[0]
#body = list(html.children)[3]
#p=list(body.children)[1]

#print(p.get_text())