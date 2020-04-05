class Kopek:
    # Class attribute
    tur = "memeli"
    # Initializer / Instance attributes
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
    # instance method
    def tanim(self):
        return "{} {} yaşında".format(self.isim, self.yas)
    # instance method
    def speak(self, ses):
        return "{} {} dedi".format(self.isim, ses)
# Child class (inherits from Köpek class)
class RussellTerrier(Kopek):
    def Kos(self, Hiz):
        return "{}  {} hızında koştu".format(self.isim, Hiz)
 
# Child class (inherits from Köpek class)
class Bulldog(Kopek):
    def Kos(self, Hiz):
        return "{}  {} hızında koştu".format(self.isim, Hiz)

class eHayvan:
    kopekler = []
    def __init__(self,kopekler):
        self.kopekler = kopekler

benim_Kopekler = [
    Bulldog("Biber",6),
    RussellTerrier("Jager",7),
    Kopek("Lassy",10)
]
# Kedi bir sınıf
# a = Kedi()

benimCocuklar = eHayvan(benim_Kopekler)
print("Benim {} köpeğim var".format(len(benimCocuklar.kopekler)))
for kopek in benimCocuklar.kopekler:
    print(f"{kopek.isim} - {kopek.yas} yaşında")

print("Elbette Hepsi {}".format(Kopek.tur))