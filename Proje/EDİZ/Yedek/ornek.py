import requests
from bs4 import BeautifulSoup
sayfa = requests.get("https://raw.githubusercontent.com/vektorelpython19/pythontemel/master/Proje/ED%C4%B0Z/B15_9.html")
soup = BeautifulSoup(sayfa.content,'html.parser')
print(soup.find(id="tekbasina"))
print(soup.find_all('p')[0].get_text())

# print(sayfa.content) # ED%C4%B0Z
# print(soup.prettify())
# print(list(soup.children))
# bs4.element.tag
# liste = [type(item) for item in list(soup.children)]

# html = list(soup.children)[0]
# print(html)
# body = list(html.children)[3]
# print(body)
# p=list(body.children)[1]
# print(p)
# print(p.get_text())

