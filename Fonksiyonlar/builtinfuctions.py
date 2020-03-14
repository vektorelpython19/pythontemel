# liste = [60,50,25,45]
# print(*filter((lambda x:x>=50),liste))

# liste = [60,50,25,45,2]
# isimListe = ["Ali","Veli","İsmet","Faruk"]
# # print(*filter((lambda x:x>=50),liste))
# print(*zip(isimListe,liste))

# metin = "BEŞİKTAŞ"
# print(*enumerate(metin))

# fonk = lambda x : x*x
# liste = [1,2,3,4,5]
# for i in map(fonk,liste):
#     print(i)

import random as rand
def Notlar(puan):
    if puan in range(0,50) : return 'F'
    if puan in range(50,70) : return 'D'
    if puan in range(70,80) : return 'C'
    if puan in range(80,90) : return 'B'
    if puan in range(90,101) : return 'A'
isimListe = ["Ali","Veli","İsmet","Faruk"]
puanlar = {item:rand.randint(5,100) for item in isimListe}
print(puanlar)