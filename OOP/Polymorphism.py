# gömülü fonksiyonlarda polimorfizm
metin = "Python"
liste = ["1",1,2,3]
print(len(metin))
print(len(liste))
# kullanıcı tanımlı fonksiyonlarda polimorfizm
def fonk(a,b,c=0):
    return a + b + c
print(fonk(1,2))
print(fonk(1,2,3))
# Sınıf Metodlarında Polimorfizm
class Ulke1:
    def yer():
        print("Ülke Asya Kıtasında")
    def nufus():
        print("Gittikçe Azalıyor")
    def type():
        print("Cumhuriyet")
class Ulke2:
    def yer():
        print("Ülke Avrupa Kıtasında")
    def nufus():
        print("25 Milyon")
    def type():
        print("Cumhuriyet")

def Fonk(nesne):
    nesne.yer()
    nesne.nufus()
    nesne.type()

for item in (Ulke1,Ulke2):
    Fonk(item)
#----------------------------------------
class A:
    def fonk1(self):
        print("A uzerinden calisti")
class B(A):
    def fonk1(self):
        print("B uzerinden calisti")
        # super(A,self).fonk1()
class C(B):
    def fonk1(self):
        print("C uzerinden calisti")
        super(B,self).fonk1()

for item in (A,B,C):
    item().fonk1()


#-------------------------------------------
class A:
    def __init__(self):
        self.a = 2
    
    def fonk1(self):
        return self.a
class B(A):
    def __init__(self):
        self.b = 3

    def fonk1(self):
        return self.b 
nesneb = B()