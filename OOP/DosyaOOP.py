
class DosyaTool:
    dosyaUzantisi = ".csv"
    def __init__(self,adres,dosyaadi="teldefter",alanlar=["Adı","Soyadı","Tel"]):
        self.dosyaadi = dosyaadi
        self.adres = adres
        self.dosya = None
        self.DosyaAc()
        self.icerik = self.dosya.readlines()
        self.alanlar = alanlar
    
    def DosyaAc(self):
        import os
        tamAdres = self.adres + os.sep + self.dosyaadi + DosyaTool.dosyaUzantisi
        if os.path.exists(tamAdres):
            self.dosya = open(tamAdres,"r+")
        else:
            self.dosya = open(tamAdres,"w+")
    
    
    def kayitAl(self):
        kayit = ""
        for item in self.alanlar:
            kayit += input(item + " Giriniz:") + ";"
        else:
            kayit.rstrip(";") + "\n"
        return kayit
        #Ali;Veli;123123
    def kayitListe(self):
        adim = 0
        for item in self.icerik:
            print(adim,end="-")
            print(*item.split(";"))
            #0 - Ali;Veli;123123

    def Ekleme(self):
        self.icerik.append(self.kayitAl())
    
    def Duzeltme(self):
        self.kayitListe()
        self.icerik[int(input("Düzenlemek istediğiniz kaydı seçiniz"))] = self.kayitAl()
    
    def Silme(self):
        self.kayitListe()
        del self.icerik[int(input("Silmek istediğiniz kaydı seçiniz"))]

    def Kaydet(self):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(self.icerik)
        self.dosya.close()
    
    def Menu(self):
        menu ="""
        1-Ekleme
        2-Silme
        3-Güncelleme
        4-Listeleme
        5-Çıkış
        Seçim Yapınız:
        """
        islem = 0
        while 0<=islem<5:
            islem = int(input(menu))
            liste = [self.Ekleme,self.Silme,self.Duzeltme,self.kayitListe,]
            liste[islem-1]()
        else:
            print("İyi Günler")    

      

    def __del__(self):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(self.icerik)
        self.dosya.close()


teldefter = DosyaTool(adres=r"d:")
teldefter.Ekleme()
teldefter.Ekleme()
teldefter.Duzeltme()

#Banka Defter
#bankadefter
#alanlar hesapadi,hesaptur,tutar,geldigitti 