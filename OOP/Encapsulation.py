class A:
    def __init__(self):
        self.__gizli = 1   #encapsulation
        
    def gizlidegistir(self,deger):
        if isinstance(deger,str):
            if deger.isnumeric():
                self.__gizli = deger
    
    def gizliGetir(self):
        return self.__gizli
            


a = A() # instantiaon
a.gizliGetir()
a.gizlidegistir("2")
a.gizliGetir()


# Access Modifiers
# private
# public
# static

#getter
#setter


# __gizli_
# __gizli
# # __gizli__

# inheritance
class A:
    def __init__(self):
        self.a = "Normal"
        self._b = "Korumalı"
        self.__c = "Gizli"
class B(A):
    def __init__(self):
        self.b = "Normal"
        A.__init__(self)

Obj1 = A()
Obj2 = B()
print(Obj2._b)