import sys
import requests
import os 
import datetime
import time
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5 import uic
from DB.DB1 import DataEmlak

class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Proje\EDİZ\Emlak\ProjeUI_1.ui",self)
        self.dbEmlak = DataEmlak()
        # self.VeriCek("ankara","cankaya",5)
        self.Goster()

    def Goster(self):
        self.ilDoldur()
        self.prgCekim.setValue(0)
        self.btVeriCek.clicked.connect(self.VeriHazir)
        self.prgCekim.valueChanged.connect(self.Yenile)
        self.cmbil.currentIndexChanged.connect(self.ilcedoldur)
        self.show()

    def karakterDuzelt(self,metin):
        karset = {"ş":"s","ç":"c","ö":"o","ü":"u","ı":"i","ğ":"g"}
        sonuc = ""
        for i in metin:
            if karset.get(i):
                sonuc += karset.get(i)
            else:
                sonuc += i
        return sonuc

    def VeriHazir(self):
        self.prgCekim.setValue(0)
        il = self.karakterDuzelt(self.cmbil.currentText().lower())
        ilce = self.karakterDuzelt(self.cmbilce.currentText().lower())
        self.VeriCek(il,ilce,5)

    def ilDoldur(self):
        liste = self.dbEmlak.ilListele()
        self.ilListeDict = {}
        self.cmbil.addItem("Seçiniz","-1")
        for item in liste:
            self.cmbil.addItem(item[1],item[0])
            self.ilListeDict[item[1]] = item[0]

    def ilcedoldur(self):
        liste = self.dbEmlak.ilceListele(self.ilListeDict[self.cmbil.currentText()])
        self.cmbilce.clear()
        self.cmbilce.addItem("Seçiniz","-1")
        for item in liste:
            self.cmbilce.addItem(item[1],item[0])

    def ListeBilgisiEkle(self,mesaj="deneme"):
        self.Rapor.addItem(mesaj)
        self.Rapor.repaint()

    def Yenile(self):
        self.Rapor.setFocus()

    def VeriCek(self,il,ilce,adim):
        tarih = datetime.datetime.today()
        dosyaadi = f"{il}_{ilce}_{tarih.day}_{tarih.month}_{tarih.year}.csv"
        adres = "Proje\\EDİZ\\Emlak\\Data\\"+dosyaadi
        dosya = open("Proje\\EDİZ\\Emlak\\Data\\"+dosyaadi,"w+",encoding="UTF-8")
        self.ListeBilgisiEkle(f"{il},{ilce}")
        self.ListeBilgisiEkle(f"Dosyayı Açtım :{adres}")
        for j in range(adim):
            time.sleep(2)            
            HEADERS = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            }
            url = f'https://www.sahibinden.com/satilik-daire/{il}-{ilce}?pagingOffset={j*5}'
            sayfa = requests.get(url, timeout=300,headers=HEADERS)
            self.ListeBilgisiEkle(f"Çekim %{(j+1)*20}")
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(sayfa.content,"html.parser")
            liste2 = soup.findAll("td",class_="searchResultsAttributeValue")
            liste3 = soup.findAll("td",class_="searchResultsPriceValue")
            liste4 = soup.findAll("td",class_="searchResultsDateValue")
            liste5 = soup.findAll("td",class_="searchResultsLocationValue")
            listeOda = []
            listem2 = []
            
            for i in range(len(liste2)):
                if i % 2==0:
                    listem2.append(liste2[i])
                else:
                    listeOda.append(liste2[i])
           
                    
            for i in range(len(liste3)):
                if self.chkM2.isChecked():
                    m2 = listem2[i].text.replace("\n"," ").strip()
                else:
                    m2 = 0
                if self.chkOda.isChecked():
                    oda = listeOda[i].text.replace("\n"," ").strip()
                else:
                    oda = 0
                if self.chkCost.isChecked():
                    fiyat = liste3[i].text.replace("\n"," ").strip()
                else:
                    fiyat = 0
                tarih = liste4[i].text.replace("\n"," ").strip()
                lokasyon = liste5[i].text.replace("\n","\\").replace(" ","")
                print(f"{m2};{oda};{fiyat};{tarih};{lokasyon}",file=dosya)
            self.prgCekim.setValue((j+1)*20)
        self.ListeBilgisiEkle("Tamamlandı")
        # print(len(liste2),len(liste3))

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())
