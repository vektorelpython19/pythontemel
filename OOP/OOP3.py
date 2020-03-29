# --attribute--
    # isim
    # yetenek
    # guc
    # saglik
    # aktif 
# --method--
    # vurus
    # darbe

class MarvelHero:
    tip = "Marvel"
    def __init__(self,isim,yetenek,guc,saglik):
        self.isim = isim
        self.yetenek = yetenek
        self.guc = guc
        self.saglik = saglik
        self.aktif = 1
    
    def vurus1(self):
        print(self.isim,"Vurus1 Kullandı")
        return self.guc
    def vurus2(self):
        print(self.isim,"Vurus2 Kullandı")
        return int(self.guc*(2/3))
    def vurus3(self):
        print(self.isim,"Vurus3 Kullandı")
        return int(self.guc*(1/3))

    def darbe(self,etki):
        self.saglik -= etki
        print(self.isim,self.saglik)
    
    def savunma(self,etki):
        self.saglik -= etki//2
        print(self.isim,self.saglik)


    def yetenekKullan(self,rakip):
        print(self.isim,self.yetenek,"kullandı")

    
    def durum(self):
        print(self.isim,self.saglik)



class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__("DeadPool","Yenilenme",65,1000)
    
    def darbe(self,etki):
        self.saglik -= etki/2
        print(self.isim,self.saglik)
    
class IronMan(MarvelHero):
    def __init__(self):
        super().__init__("IronMan","Enerji Patlaması",65,1200)
    
    def vurus(self):
        print(self.isim,"Güç Kullandı")
        return self.guc*2
    
class SpiderMan(MarvelHero):
    def __init__(self):
        super().__init__("SpiderMan","AltıncıHis",50,1000)

class CaptainMarvel(MarvelHero):
    def __init__(self):
        super().__init__("CaptainMarvel","Photon Blast",75,1000)


class WonderWoman(MarvelHero):
    def __init__(self):
        super().__init__("Princess Diana","Dayaniklilik",60,1000)
        self.aktif = 0
  

class Beyonder(MarvelHero):
    def __init__(self):
        super().__init__("Beyonder","Gerceklik Kontrolü",50000,500000)
    

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk","Guc",400000000,600)
    
class BlackWidow(MarvelHero):
    def __init__(self):
        super().__init__("Natasha","Kılık Değiştirme",80,1000)

if __name__ == "__main__":
    pass