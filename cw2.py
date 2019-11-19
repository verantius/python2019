#doda 4 imiona
#jezeli kara to wysfietli w ktorym rzedzie
#karo musi byc pierwsza

lista=[]

n = int(input("podaj lie imion chcesz podac: "))
for i in range (1,n+1):
    x = input("pdaj imie:> ")
    p=x.lower()
    lista.append(p)

print("\n")
for y in lista:
    print(y)
print("\n")
d = len(lista)
print("ilosc elementow w d to ",d)
if "kara" in lista:
    lista.remove("kara")
    lista.insert(0,"kara")
kara=lista.index("kara")
kara+=1

print("Kara jest w %d miejscu"%kara)
for y in lista:
    print(y)