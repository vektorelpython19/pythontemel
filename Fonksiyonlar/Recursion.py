metin = "BEŞİKTAŞ"
def reco(metin):
    if len(metin) == 1:
        print(metin)
    else:
        print(metin)
        reco(metin[1:])
        print(metin)

reco(metin)