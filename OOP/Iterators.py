# demet = (1,2,3,4,5)
# # liste,metin
# benimIter = iter(demet)
# print(next(benimIter))
# print(next(benimIter))
# print(next(benimIter))
# print(next(benimIter))
# for item in demet:
#     print(item)



class benimAlfabe:
    def __init__(self):
        self.alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
        self.alfabe = [i for i in self.alfabe]
        print(self.alfabe)
    def __iter__(self):
        self.adim = 0
        return self
    def __next__(self):
        if self.adim < len(self.alfabe):
            karakter = self.alfabe[self.adim]
            self.adim += 1
            return karakter
        else:
            raise StopIteration

nesne1 = benimAlfabe()
benimIter = iter(nesne1)
print(next(benimIter))
print(next(benimIter))
