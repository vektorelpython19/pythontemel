# class A:
#     sinif_ozellik = "A"
#     def __init__(self):
#         self.a = "a"
    
#     def ornekMetod(self):
#         return self.a 

#     @classmethod
#     def sinifmetod(cls):
#         return cls.sinif_ozellik

#     @staticmethod
#     def statik():
#         return 22//7

# print(A.sinifmetod())
# print(A.statik())
# nesne1 = A()
# print(nesne1.sinifmetod())
# print(nesne1.statik())


    

import time
import math
def hesapZaman(fonk):
    def icFonk(*args,**kwargs):
        baslangic = time.time()
        fonk(*args,**kwargs)
        bitis = time.time()
        print("Bu işlem çalışma zamanı",fonk.__name__,bitis-baslangic)
    return icFonk

@hesapZaman
def Faktoriyel(param):
    time.sleep(2)
    print(math.factorial(param))

Faktoriyel(10)