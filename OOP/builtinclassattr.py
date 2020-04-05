class A:
    """
    bu sınıf built in 
    class attribute elemanlardan 
    bir kaçını göstermek için yapılmıştır
    """
    sinifOz = 0
    def __init__(self, adi,soyadi):
        self.adi = adi
        self.soyadi = soyadi
        A.sinifOz += 1
    
    def goruntule(self):
        """açıklama"""
        print("Toplam",A.sinifOz)

    def OrnekGoruntule(self):
        print(self.adi,self.soyadi)
    
print("A.__doc__",A.__doc__)
print("A.__name__",A.__name__)
print("A.__module__",A.__module__)
print("A.__bases__",A.__bases__)
print("A.__dict__",A.__dict__)
nesne = A("a","b")
print(nesne.goruntule.__doc__)