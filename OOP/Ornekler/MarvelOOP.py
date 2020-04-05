class MarvelHero:
    tip = "Marvel"
    def __init__(self,isim,yetenek,guc,saglik):
        self.isim = isim
        self.yetenek = yetenek
        self.guc = guc
        self.saglik = saglik
        self.aktif = 1
        self.OfansList  = [self.vurus1,self.vurus2,self.vurus3]
        self.DefansList = [self.savunma,self.darbe]
    def vurus1(self):
        return self.guc
    def vurus2(self):
        return int(self.guc*(2/3))
    def vurus3(self):
        return int(self.guc*(1/3))

    def darbe(self,etki):
        self.saglik -= etki
    
    def savunma(self,etki):
        self.saglik -= etki//2


    def yetenekKullan(self,rakip):
        print(self.isim,self.yetenek,"kullandı")

    def Ofans(self):
        import random as rnd

        liste = [self.vurus1,self.vurus2,self.vurus3]
        return rnd.choice(liste)()
                    
    def Defans(self,etki):
        import random as rnd
        DefansListe = [self.savunma,self.darbe]
        return rnd.choice(DefansListe)(etki)


    def durum(self):
        print(self.isim,self.saglik)

class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__("DeadPool","Yenilenme",65,1000)
    
    def darbe(self,etki):
        self.saglik -= etki//2

class IronMan(MarvelHero):
    def __init__(self):
        super().__init__("IronMan","Enerji Patlaması",65,1200)
    
    def vurus1(self):
        return self.guc*2

class SpiderMan(MarvelHero):
    def __init__(self):
        super().__init__("SpiderMan","AltıncıHis",50,1000)

class CaptainMarvel(MarvelHero):
    def __init__(self):
        super().__init__("CaptainMarvel","Photon Blast",75,1000)


class WonderWoman(MarvelHero):
    def __init__(self):
        super().__init__("WonderWoman","Dayaniklilik",60,1000)
        self.aktif = 0
  

class Beyonder(MarvelHero):
    def __init__(self):
        super().__init__("Beyonder","Gerceklik Kontrolü",50,1000)
    

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk","Guc",40,60000)
    
class BlackWidow(MarvelHero):
    def __init__(self):
        super().__init__("Natasha","Kılık Değiştirme",80,1000)