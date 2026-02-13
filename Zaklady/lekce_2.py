print("hello")

odpoved = input("Tohle se napíše do řádky: ")

print(odpoved)
print(type(odpoved))

try:
    odpoved_jako_cislo = int(odpoved) #nebezpečí kombinace "str" a int
except:
    print("spatne")
    odpoved_jako_cislo = 0


# odpoved_jako_cislo = float(odpoed)


print("ahoj " + "vole")
print(22 + odpoved_jako_cislo)
