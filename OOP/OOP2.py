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
    
    def vurus(self):
        return self.guc

    def darbe(self,etki):
        self.saglik -= etki

    def yetenekKullan(self,rakip):
        print(self.isim,self.yetenek,"kullandı")

    


class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__("DeadPool","Yenilenme",65,1000)
    
    def darbe(self,etki):
        self.saglik -= etki/2
    
class IronMan(MarvelHero):
    def __init__(self):
        super().__init__("IronMan","Enerji Patlaması",65,1200)
    
    def vurus(self):
        return self.guc
    
class SpiderMan(MarvelHero):
    def __init__(self):
        super().__init__("SpiderMan","AltıncıHis",50,1000)

class CaptainMarvel(MarvelHero):
    def __init__(self):
        super().__init__("CaptainMarvel","Photon Blast",75,1000)


class WonderWoman(MarvelHero):
    def __init__(self):
        super().__init__("Princess Diana","Dayaniklilik",60,1000)
  

class Beyonder(MarvelHero):
    def __init__(self):
        super().__init__("Beyonder","Gerceklik Kontrolü",50000,500000)
    

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk","Guc",400000000,600)
    
class BlackWidow(MarvelHero):
    def __init__(self):
        super().__init__("Natasha","Kılık Değiştirme",80,1000)