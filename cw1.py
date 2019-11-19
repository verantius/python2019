#doda 4 imiona
#znajdzie marte i usunie
#jezeli kara to wysfietli w ktorym rzedzie
#karo musi byc pierwsza

lista=[]
def check_name(name):
    return name in lista

n = int(input("Podaj ilosc imion:\n>"))

for i in range (1,n+1):
#while n:
    imie = input("podaj imie:> ")
    lista.append(imie)
    if "kara" in lista:
        tutaj=i
        #print("kara jest w ",i,"kolejnosci")
   # n -= 1
print("\n")
for i,y in enumerate (lista):
    print(y)

if "magda" in lista:
    lista.remove("magda")
#lista.reverse()
print("\n")
print("czy adam jest z nami: ",check_name("adam"))
print("\n")
for y in lista:
    print(y)
karhere = lista.index("kara")
karhere+=1
print("kara jest w:%d:miejscu \n"%karhere)



