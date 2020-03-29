class A:
    Sinif_Ozellik = ""
    def __init__(self,*args,**kwargs): #Constructor
        print("Nesne Üretildi")
        self.ornek_ozellik = "Örnek1"
    
    def __del__(self): #Destructor
        print("Hoşçakal")

a = A()