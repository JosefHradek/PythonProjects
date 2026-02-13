vstup = input("zadej číslo: ")
try:
    cislo = int(vstup)
except:
    cislo = 0

print("vstup = " + vstup)


if cislo > 10:
    print("vetsi nez 10")
if (cislo > 10) and (cislo < 20):  #  10 < cislo < 20
    print("je vetsi nez 10 ale mensi nez 20")
if cislo % 2 == 0:
    print("sude")
else:
    print("liche")