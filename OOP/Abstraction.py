from abc import  abstractmethod,ABC
# Abstract Base Class

class Araclar(ABC): #abstraction
    @abstractmethod
    def IleriGit(self):
        pass
    @abstractmethod 
    def Dur(self):
        pass 


class DenizAraclari(Araclar):
    def __init__(self):
        self.Plaka = "2"
    
    def Dur(self):
        pass

    def IleriGit(self):
        pass
