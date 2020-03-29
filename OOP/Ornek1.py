# Hayvan Ana Class
# Kedi  Child Class
# Kopek  Child Class
# her sınıfta gizli bir değişken

#Mert Akkor
# class Hayvan:
#     def __init__(self):
#         self.__hayvanlar = "Hepsi hayvan"
#         self.__seslenme = "___"

# class Kedi(Hayvan):
#     def __init__(self):
#         super().__init__()
#         self.__seslenme = "Miyavladı"

# class Kopek(Hayvan):
#     def __init__(self):
#         super().__init__()
#         self.__seslenme = "Havladı"

# Kopek()
# Kedi()

#Yekta Sökelen
class Hayvan:
    def __init__(self):
        self.__hayvanlar = "Hayvan"
        self.__ses=""
        
    def sesCikar(self):
        return self.__ses

class Horoz(Hayvan):
    def __init__(self):
        super().__init__()
        self.__ses= "Ottu"

class Tavuk(Hayvan):
    def __init__(self):
        super().__init__()
        self.__ses = "ses yok"

kus1 = Horoz()
kus2 = Tavuk()
print(kus1.sesCikar())
print(kus2.sesCikar())