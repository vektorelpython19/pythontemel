class A:
    def fonk1(self):
        print("A uzerinden calisti")
class B(A):
    def fonk1(self):
        print("B uzerinden calisti")
        super().fonk1()
class C(B):
    def fonk1(self):
        print("C uzerinden calisti")
        super(B,self).fonk1()

for item in (A,B):
    item().fonk1()