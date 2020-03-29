# Inheritance

class A:
    def __init__(self):
        self.__gizli = 1
        self.a = "A"
    
    def aFonk(self):
        return 1

class B(A):
    def __init__(self):
        super().__init__()
        self.b = "B"


class C(B):
    def __init__(self):
        super().__init__()
        self.c = "C"

class D:
    def __init__(self):
        self.d = "D"
class D_1:
    def __init__(self):
        self.d_1 = "D_1"


class E(A,D):
    def __init__(self):
        # super().__init__() #A
        A.__init__(self)
        D.__init__(self)
        self.e = "E"

class F(D,D_1):
    def __init__(self):
        D.__init__(self)
        D_1.__init__(self)
        self.f = "F"




nesneA = A()
nesneB = B()
nesneC = C()
nesneD = D()
nesneD_1 = D_1()
nesneE = E()
nesneF = F()
print(type(nesneA))
print(type(nesneB))
print(type(nesneC))
print(type(nesneD))
print(type(nesneD_1))
print(type(nesneE))
print(type(nesneF))
print(isinstance(nesneA,C))
print(isinstance(nesneC,A))
print(issubclass(D_1,C))
print(issubclass(E,D))



# Acaba  --------------- # 
# class A_1:
#     def __init__(self):
#         self.a = "A"
# class B_1(A_1):
#     def __init__(self):
#         super().__init__()
#         self.b = "B"
# class A_1(B_1):
#     def __init__(self):
#         super().__init__()
#         self.c = "C"
# nesne1 = A_1()
# print(nesne1.a)
# print(nesne1.b)
# print(nesne1.c)


