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

# import random as rand
# rand.seed(5)
# def Notlar(puan):
#     if puan in range(0,50) : return 'F'
#     if puan in range(50,70) : return 'D'
#     if puan in range(70,80) : return 'C'
#     if puan in range(80,90) : return 'B'
#     if puan in range(90,101) : return 'A'
# isimListe = ["Ali","Veli","İsmet","Faruk"]
# puanlar = {item:rand.randint(5,100) for item in isimListe}
# print(*map(Notlar,puanlar.values()))
# for a,b in zip(puanlar.keys(),map(Notlar,puanlar.values())):
#     print(a,b,puanlar[a])

# metin = "AF675-2346H-Vektorel"
# print(hash(metin))


# metin = "python"
# print(isinstance(metin,str))

# print(divmod(7,2))

# a = bytes("Aython","ascii")
# print(*a)
# a = bytearray("Aython","ascii")
# print(*a)
# a[0] = 115
# print(a)
# metin = ascii(a)
# print(ascii("Şermin"))
# print(repr("Şermin"))

# print(*globals().values(),sep="\n")

# b = 3
# def Fonk():
#     b = 5
#     a = 8
#     print(locals())
# Fonk()
# def Suz(x):
#     return not x.startswith("__")
# print(*filter(Suz,globals()["__builtins__"]),sep="\n")


# liste = [2,3,4,5,9,8,7,5]
# # liste.sort()
# # liste.reverse()
# # print(liste)
# print(*reversed(liste))
# print(*sorted(liste))
# print(liste)
