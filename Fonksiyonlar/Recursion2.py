#recursion
def Fibanocci(n):
    if n<0:
        print("Geçersiz Giriş")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibanocci(n-1)+Fibanocci(n-2)
#dynamic
FibArray = [0,1]
def fibanocci(n):
    if n<0:
        print("Geçersiz Giriş")
    elif n<=(len(FibArray)):
        return FibArray[n-1]
    else:
        temp_fib = fibanocci(n-1)+fibanocci(n-2)
        FibArray.append(temp_fib)
        return temp_fib
#space optimized
def fibanocci(n):
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