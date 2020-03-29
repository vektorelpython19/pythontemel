# class Araçlar:
#     def __init__(self):
#         self.__araclar = 1
#         self.araclar = "Araçlar"
# class KaraAraçları(Araçlar):
#     def __init__(self):
#         super().__init__()
#         self.karaAracları = "Karada Kullanılanlar"
# class BinekAraçlar(KaraAraçları):
#     def __init__(self):
#         super().__init__()
#         self.binekAracları = "Oturmalı"
# class Otomobil(BinekAraçlar):
#     def __init__(self):
#         super().__init__()
#         self.otomobil = "Kişiye Özel"


# class Araclar:
#     def __init__(self):
#         self.KaraAraclar = "Binek Araçlar"
#         self.__DenizAraclar = "Deniz Araçları"
#         self.__HavaAraclar = "Hava Araçları"

# class KaraAraclar(Araclar):
#     def __init__(self):
#         super().__init__()
#         self.BinekAraclar = "Binek Araçlar"
#         self.__YukAraclar = "Yük ARaçları"
#         self.__Diger = "Diğer"

# class BinekAraclar(KaraAraclar):

#     def __init__(self):
#         super().__init__()
#         self.Otomobil = "Otomobiller iyidir"
#         self.__TopluTasima = "Toplu taşıma"

#     def CoronoOlma(self):
#         print("Otomobil kullan.")

# kara = KaraAraclar()
# binek = BinekAraclar()
from abc import  abstractmethod,ABC
# Abstract Base Class

class Araclar(ABC): #abstraction
    @abstractmethod
    def IleriGit(self):
        pass
    @abstractmethod 
    def Dur(self):
        pass 


class DenizAraclari(Araclar):
    def __init__(self):
        self.Plaka = "2"
    
    def Dur(self):
        pass

    def IleriGit(self):
        pass

arac1 = DenizAraclari()
arac1.Dur()

class KaraAraclari(Araclar):
    def __init__(self,tekerSayisi,yakitTuru,motorGucu,Plaka):
        self.tekerSayisi = tekerSayisi
        self.yakitTuru = yakitTuru
        self.motorGucu = motorGucu
        self.Plaka = Plaka

    def ParkEt(self):
        self.Dur()
        print(self.Plaka,"Park Etti")
    
    def Dur(self):
        print(self.Plaka,"Durdu")
    
    def IleriGit(self):
        print(self.Plaka,"İleri Gitti")

    def GeriGit(self):
        print(self.Plaka,"Geri Gitti")



class BinekAraclar(KaraAraclari): #inheritance
    def __init__(self,tekerSayisi,yakitTuru,motorGucu,Plaka,koltukSayisi,KapiSayisi):
        super().__init__(tekerSayisi,yakitTuru,motorGucu,Plaka)
        self.KoltukSayisi = koltukSayisi
        self.KapiSayisi = KapiSayisi

    def KapiAc(self):
        print(self.Plaka,"Kapı Açıldı")

    def Dur(self): #polymorphism
        print(self.Plaka,"Yavaşlayarak Durdu")


class Otomobil(BinekAraclar): 
    def __init__(self,yakitTuru,MotorGucu,Plaka,KoltukSayisi,KapıSayisi,Marka,Model,Renk):
        super().__init__(4,yakitTuru,MotorGucu,Plaka,KoltukSayisi,KapıSayisi)
        self.Marka = Marka
        self.Model = Model
        self.Renk = Renk
    
    def Rolanti(self):
        pass

    def Hareket(self,yon):
        if yon == "N":
            self.Rolanti()
        elif yon == "R":
            self.GeriGit()
        elif yon == "D":
            self.IleriGit()
        elif yon == "P":
            self.ParkEt()

class Arac1(Otomobil):
    def __init__(self):
        super().__init__("LPG",75,"06DRBDR06",4,5,"Tofaş","Şahin","Beyaz")
arac1 = Arac1()
arac1.Hareket("D")



