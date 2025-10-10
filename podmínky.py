vstup = input("zadej číslo: ")
try:
    cislo = int(vstup)
except:
    cislo = 0

print("vstup = " + vstup)

if cislo > 5:
    print("cislo")
    print(cislo)
    print("je")
    print("větší než 5")
    if cislo >10:
        print("nevim, neco")
else:
    print("neni vetsi nez 5")
if cislo < 7:
    print("cislo je mensi nez 7")

print("konec")

a = input("zadej A: ")
b = input("zadej B: ")
c = input("zadej C: ")

if b ** 2 < 4*a*c:
    print("nula reseni")
elif b ** 2 == 4 * a * c:#neco spatne
    print("jedno reseni")
else:
    print("dve reseni")