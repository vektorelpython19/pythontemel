from MarvelOOP import *
import time
import random as rnd
class Oyun:
    karList = [DeadPool,IronMan,
        WonderWoman,SpiderMan,CaptainMarvel,Beyonder,Hulk,BlackWidow]
    def __init__(self):
        pass
    
    def PCvsPC(self):
        P1 = rnd.choice(Oyun.karList)()
        P2 = rnd.choice(Oyun.karList)()
        print(P1.isim,"vs",P2.isim)

        while P1.saglik > 0 and P2.saglik > 0:
            time.sleep(1)
            P1.Defans(P2.Ofans())
            P2.Defans(P1.Ofans())
            print(f"{P1.isim}-{P1.saglik}vs{P2.isim}-{P2.saglik}")
        else:
            if P1.saglik > P2.saglik:
                print(P1.isim,"Kazandı")
            else:
                print(P2.isim,"Kazandı")

    def Listele(self,liste,mesaj):
        for i in range(len(liste)):
            print(f"{i+1}-{liste[i].__name__}")
        return int(input(mesaj + " Seç"))-1  


    def USERvsPC(self):
        P1 = rnd.choice(Oyun.karList)()
        P2 = Oyun.karList[self.Listele(Oyun.karList," Karakterini")]()
        while P1.saglik > 0 and P2.saglik > 0:
            time.sleep(1)
            P1.Defans(P2.OfansList[self.Listele(P2.OfansList,"Ofansif Hareketini ")]())
            P2.DefansList[self.Listele(P2.DefansList,"Defansif Hareketini ")](P1.Ofans())
            print(f"{P1.isim}-{P1.saglik}vs{P2.isim}-{P2.saglik}")

    def USERvsUSER(self):
        P1 = Oyun.karList[self.Listele(Oyun.karList,"P1 Karakterini")]()
        P2 = Oyun.karList[self.Listele(Oyun.karList,"P2 Karakterini")]()
        while P1.saglik > 0 and P2.saglik > 0:
            time.sleep(1)
            P1.DefansList[self.Listele(P1.DefansList,"P1 Defansif Hareketini ")](P2.OfansList[Listele(P2.OfansList,"P2 Ofansif Hareketini ")]())
            P2.DefansList[self.Listele(P2.DefansList,"P2 Defansif Hareketini ")](P1.OfansList[Listele(P1.OfansList,"P1 Ofansif Hareketini ")]())
            print(f"{P1.isim}-{P1.saglik}vs{P2.isim}-{P2.saglik}")
