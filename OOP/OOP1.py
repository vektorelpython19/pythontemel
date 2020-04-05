# 1
# class Kedi:
#     adi = ""
#     yas = 0
#     def Miyavla():
#         print("aaa")

# 2
class Kedi:
    tur = "Felix" #class attribute
    def __init__(self,adi,yasi): #constructor yapıcı
        self.adi = adi #instance attribute
        self.yasi = yasi #instance attribute
        # print(self.adi,"Doğdu")

    def Miyavla(self): # instance method
        print(self.adi,"Miyavladi")

    def __del__(self):
        self.Miyavla()
        print(self.adi,"Huzur içinde uyu")
# garbage collector

# Kedi("Melek",2).Miyavla()
kedi1 = Kedi("Melek",2) #instantiation
kedi2 = Kedi("Misket",3)
del kedi1
print(kedi2.adi)



