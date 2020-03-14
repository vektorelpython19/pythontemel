#recursion
def fibanocci1(n):
    if n<0:
        print("Geçersiz Giriş")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibanocci1(n-1)+fibanocci1(n-2)
# fibanocci1(2)
#dynamic
FibArray = [0,1]
def fibanocci2(n):
    if n<0:
        print("Geçersiz Giriş")
    elif n<=(len(FibArray)):
        return FibArray[n-1]
    else:
        temp_fib = fibanocci2(n-1)+fibanocci2(n-2)
        FibArray.append(temp_fib)
        return temp_fib
fibanocci2(9)
#space optimized
def fibanocci3(n):
    a = 0
    b = 1
    if n<0:
        print("Geçersiz Giriş")
    elif n==0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c=a+b
            a,b=b,c
        return b

def islemZaman(fonk,param):
    import time
    baslangic = time.time()
    print(fonk(param))
    simdi = time.time() - baslangic
    print(round(simdi,4))
# n = 40
# # islemZaman(fibanocci1,n)
# islemZaman(fibanocci2,n)
# # islemZaman(fibanocci3,n)