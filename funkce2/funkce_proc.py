

a = 5
def max_2(s):
    if s[0] > s[1]:
        maxim = s[0]
        max2 = s[1]
    else:
        maxim = s[1]
        max2 = s[0]
    for i in range(len(s)):
        if s[i] > maxim:
            max2 = maxim
            maxim = s[i]
        if s[i] > max2 and s[i] < maxim:
            max2 = s[i]
    return max2

seznam = [10,5,7,8,19,2,10,2,15,2,19]
print((a-1)*" " + str(max_2(seznam)))

for i in range (a):
    print((a-i)*" "+i*"/"+i*"\\"+(a-i)*" ")
for i in range(round(a/2)):
    print((a-1)*" "+"||"+(a-1)*" ")

def prvo(a):
    for i in range (2,a):
        if a%i == 0:
            return False
    return True

print(prvo(5))



def prvo(a):
    for i in range (2,a):
        if a%i == 0:
            return False
    return True
#@<>[]{}()
vstup=[5,13,31,55,17,54,2,6]

def poc_pr(vstup):
    poc = 0
    for j in range(len(vstup)):
        if prvo(vstup[j]):
            poc += 1
    return poc

print (poc_pr(vstup))


def adding (a,b):
    return a+b

def odecitani(a,b):
    return a - b

def pocitej (funkce,a,b):
    return funkce(a,b)


print (pocitej(adding,5,3))


pejsek = int(input("zadej cislo"))
kocicka = int(input("zadej 2 cislo"))
ptacek = input("zadej fukci ")

if ptacek == "+":
    print(pocitej(adding, pejsek, kocicka))
elif ptacek == "-":
    print(pocitej(odecitani, pejsek, kocicka))
else:
    print("neznama funkce")