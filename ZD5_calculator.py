def calc(a,b,l):
    if l == "+":
        return a+b
    elif l == "-":
        return a-b
    elif l == "*":
        return a*b
    elif l == "/":
        return a/b
    else:
        return "invalid operator! "



print("wynik wynosi: ",calc(2,3,"s"))