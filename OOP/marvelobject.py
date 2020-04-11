from marvelheroOOP import *
import time
import random as rnd
karList = [DeadPool,IronMan,WonderWoman,SpiderMan,CaptainMarvel,Beyonder,Hulk,BlackWidow]
P1 = rnd.choice(karList)()
P2 = rnd.choice(karList)()
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
def Listele(liste):
    for i in range(len(liste)):
        print(f"{i+1}-{liste[i].__name__}")
    return int(input(mesaj+"Seç"))-1    


def USERvsPC:
     karList = [DeadPool,IronMan,WonderWoman,SpiderMan,CaptainMarvel,Beyonder,Hulk,BlackWidow]
     P1 = rnd.choice(karList)()
     P2 = rnd.choice(karList)()
     while P1.saglik > 0 and P2.saglik > 0:
         
