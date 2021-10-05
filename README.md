# Arduino Pythonem

'''
a = float(input("Zadej prvni cislo: "))
b = float(input("Zadej druhe cislo: "))
operace = input("Zadej operaci: ")
vysledek = 0


def porovnavani(a,b):
    if a > b:
        print("Prvni cislo je vetsi!")
    elif b > a:
        print("Druhe cislo je vetsi!")
    else:
        print("Cisla se rovnaji!")

def pocitej(a,b,operace):
    if operace == "+":
        vysledek = a + b
    elif operace == "-":
        vysledek = a - b
    elif operace == "*":
        vysledek = a * b
    elif operace == "/":
        vysledek = a / b
    else:
        print("Zadavej pouze + - * /")

    print("Vysledek = " + str(vysledek))


print("Kalkulacka na pocitani a porovnavani")
pocitej(a,b,operace)
porovnavani(a,b)
print("Hotovo")

'''
