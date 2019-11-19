#### 3. Napisz program, w którym
# Pobieraj od użytkownika wyrazy tak długo aż poda "koniec".
# Wyrazy odkładaj na listę
# Wypisz na ekran wyrazy w kolejności odwrotnej niż pobierana (ostatni jako pierwszy). Nie wypisuj słowa "koniec".
lista=[]

x = input("Podaj dzień tygodnia: ")
lista.append(x)

while (x!="koniec"):
    x = input("Podaj dzień tygodnia: ")
    lista.append(x)
lista.remove("koniec")
lista.reverse()

print("Podales koniec!!\n")


for i, y in enumerate(lista):
    print(y)

