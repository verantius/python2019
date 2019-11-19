print("\n")
x = ["ala", "marcin", "zygmunt"]
print(len(x))

x.append("zbigniew")
print(len(x))
print(x)
x.remove("marcin")
for i, y in enumerate(x):
    print("Element i", i, ": ", y)

if "zbigniew" in x:
    print("Jest zbigniew na liscie! :)")
else:
    print("kogo z nami nie ma? Zbigniewa")
print("\n")