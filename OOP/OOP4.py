from OOP3 import *
import time
import random as rnd
karList = [DeadPool,IronMan,SpiderMan,CaptainMarvel]
P1 = rnd.choice(karList)()
P2 = rnd.choice(karList)()
print(P1.isim,"vs",P2.isim)

while P1.saglik > 0 and P2.saglik > 0:
    time.sleep(1)
    P1.Defans(P2.Ofans())
    P2.Defans(P1.Ofans())
else:
    if P1.saglik > P2.saglik:
        print(P1.isim,"Kazandı")
    else:
        print(P2.isim,"Kazandı")
