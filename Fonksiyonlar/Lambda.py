def Topla(a,b):
    return a+b

fonk = lambda a,b:a+b
print(fonk(2,3))
print(Topla(2,3))

liste = ["Çiğdem","Şermin","Işınsu","Kamil","Mahmut","Ahmet"]
print(liste)
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
cevrim = {i:alfabe.index(i) for i in alfabe}
# print(cevrim[liste[0][0].lower()])
sonHal = sorted(liste,key=lambda x:cevrim.get(x[0].lower()))
print(sonHal)
print((lambda x:cevrim.get(x))("ş"))