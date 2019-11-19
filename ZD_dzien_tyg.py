#Napisać funkcję
# pobierający jeden parametr tekstowy (string) - dzień tygodnia
# zwracający cyfrę od 1 do 7. 1 gdy podamy poniedziałek, 2 - wtorek, ... 7 niedziela
# wywołać metodę podając kilka parametrów 'z ręki' lub poprzez input od użytkownika

#Niech funkcja będzie odporna na wielkość liter w prametrze -> powinno działać zarówno: poniedzialek, PonIEdzialek, Poniedzialek, PONIEDZIALEK.
#Podpowiedź: wyguglaj właściwą metodę obiektu string, która tutaj pomoże

def week(day):
    come=[]
    come.append(day)
    if day == "poniedzialek":
        print("1")
    elif day == "wtorek":
        print("2")
    elif day == "sroda":
        print("3")
    elif day == "czwartek":
        print("4")
    elif day == "piatek":
        print("5")
    elif day == "sobota":
        print("6")
    elif day == "niedziela":
        print("7")
    else:
        print("podales bledny dzien tygodnia!")


x = input("Podaj dzień tygodnia: ")
p=x.lower()
week(p)
#print("mala litera to: ",p)

