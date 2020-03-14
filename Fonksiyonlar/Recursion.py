metin = "BEŞİKTAŞ"
def reco(metin):
    if len(metin) == 1:
        print(metin)
    else:
        print(metin)
        reco(metin[1:])
        print(metin)

# reco(metin)

# 1--------------------
# a = b  = 1
# print(a+b)
# a,b = b,(a+b)
# print(a+b)
# a,b = b,(a+b)
# print(a+b)
# a,b = b,(a+b)
# print(a+b)
# a,b = b,(a+b)

# 2--------------------
# a = b = 1
# for i in range(7):
#     print(a+b)
#     a,b = b,(a+b)


# 3--------------------
# def fiboCan(sayi):
#     a = b = 1
#     for i in range(sayi):
#         print(a+b)
#         a,b = b,(a+b)
# fiboCan(7)

# 4--------------------
def rec_fibo(n):
    if n <=1:
        return n
    else:
        return(rec_fibo(n-1) + rec_fibo(n-2))

def fiboCan(sayi):
    a = b = 1
    for i in range(sayi):
        a,b = b,(a+b)
    return a+b

def islemZaman(fonk,param):
    import time
    baslangic = time.time()
    print(fonk(param))
    simdi = time.time() - baslangic
    print(round(simdi,4))

# print(rec_fibo(7))
# print(fiboCan(4))
# islemZaman(fiboCan,12)
islemZaman(rec_fibo,5)

