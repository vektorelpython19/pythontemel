class A:
    def __init__(self):
        self.__gizli = 1   #encapsulation
        self.__c = 3

    @property
    def c(self): # getter
        return self.__c

    @c.setter
    def c(self,deger):
        if isinstance(deger,str):
            if deger.isnumeric():
                deger = int(deger)
                if 10<deger<20:
                    self.__c = deger
        else:
            print("Değiştiremedim")
    
    @c.deleter
    def c(self):
        self.__c = 3



a = A() # instantiaon
print(a.c)
a.c = "15"
print(a.c)
del a.c



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