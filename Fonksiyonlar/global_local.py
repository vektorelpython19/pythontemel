# a = 5 #global
# def fonk():
#     global a
#     a = 2 #local
#     print(a)
# fonk()
# print(a)

liste = [1,2,3]
def fonk():
    liste[0] = 25
    print(liste)
fonk()
print(liste)


liste = [1,2,3]
def fonk():
    global liste
    liste = [6,7,8]
    print(liste)
fonk()
print(liste)