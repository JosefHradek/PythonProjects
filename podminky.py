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

try:
    A = int(a)
    B = int(b)
    C = int(c)
    d = B ** 2 - 4*C*A
except:
    d = "mas to spatne"

print("vysledek diskriminantu = " + str(d))

if d < 0:
    print("0 reseni")
elif d == 0:
    print("1 reseni")
else:
    print("2 reseni")