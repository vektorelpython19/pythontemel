import requests
from bs4 import BeautifulSoup
sayfa = requests.get("https://www.mgm.gov.tr/?il=Ankara&ilce=Cankaya")
soup = BeautifulSoup(sayfa.content,'html.parser')
print(soup.find_all(class_="instant-weather"))