def DosyaAc(adres="defter.csv"):
    import os
    if os.path.exists(adres):
        dosya = open(adres,"r+",encoding="utf-8")
    else:
        dosya = open(adres,"w+",encoding="utf-8")
    return dosya

def GirisAl(*args):
    kayit = ""
    for item in args:
        kayit+= input(f"{item} Giriniz:") + ";"
    else:
        kayit = kayit.rstrip(";") + "\n"
    return kayit

def KayitListele():
    for i in range(1,len(liste)+1):
        print(i,*liste[i-1].split(";"),sep="-",end="")

def KayitEkle(*args):
    kayit = GirisAl(*args)
    liste.append(kayit)

def KayitGuncelle(*args):
    KayitListele()
    secim = int(input("Düzenlemek istediğiniz kaydı seçiniz"))
    kayit = GirisAl(*args)
    liste[secim-1] = kayit

def KayitSil():
    KayitListele()
    secim = int(input("Düzenlemek istediğiniz kaydı seçiniz"))
    del liste[secim-1] 


menu = """
1-Ekleme
2-Güncelleme
3-Silme
4-Listeleme
5-Çıkış
Seçim Yapınız:"""
anahtar = 1
while anahtar == 1:
    alanlar = ["Adi","Soyadi","Tel"]
    dosya = DosyaAc()
    liste = dosya.readlines()
    islem = int(input(menu))
    if islem == 1:
        KayitEkle(*alanlar)
    elif islem == 2:
        KayitGuncelle(*alanlar)
    elif islem == 3:
        KayitSil()
    elif islem == 4:
        KayitListele()
    else:
        anahtar = 0
else:
    dosya.seek(0)
    dosya.truncate()
    dosya.writelines(liste)
    dosya.close()

Calistir()