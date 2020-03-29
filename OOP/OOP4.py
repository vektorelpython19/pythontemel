from OOP3 import *
import time

P1 = DeadPool()
P2 = IronMan()
print(P1.isim,"vs",P2.isim)
while P1.saglik > 0 and P2.saglik > 0:
    time.sleep(1)
    P1.darbe(P2.vurus())
    P2.darbe(P1.vurus())
else:
    if P1.saglik > P2.saglik:
        print(P1.isim,"Kazandı")
    else:
        print(P2.isim,"Kazandı")
