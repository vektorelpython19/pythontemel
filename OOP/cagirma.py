from DosyaOOP import  DosyaTool
teldefter = DosyaTool("OOP",dosyaadi="deneme",alanlar=["Adi","Soyadi","IşTel","CepTel"])
bankadefter = DosyaTool("OOP",dosyaadi="banka",alanlar=["BankaAdi","HesapNo","Tutar"])
teldefter.Menu()
bankadefter.Menu()
print("Adı Nedir",DosyaTool.__name__)