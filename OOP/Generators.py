import math
def GeneratorFonk(a):
    i = 0
    while i <= a:
        yield  math.factorial(i)
        i += 1

for j in GeneratorFonk(10):
    print(j)


liste = ["ali","veli","veli","ayşe","fatma","ışıl","ismail"]
from random import choice as ch
def rastGelegonder(liste,param):
    gonderilen = []
    for i in range(param):
        secilen  = ch(liste)
        while secilen in gonderilen:
            secilen  = ch(liste)
        gonderilen.append(secilen)
        yield secilen

for item in rastGelegonder(liste,3):
    print(item)