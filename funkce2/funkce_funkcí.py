def secti(a,b):
    return a+b

def odecti(a,b):
    return a-b

def vynasob_soucet_a_rozdil(a,b,c,d):
    return secti(a,b) * odecti (c,d)

def kalkulacka(a,b,funkce):
    return funkce(a,b)

print ("vysledek (a+b) * (c-d) = " + str(vynasob_soucet_a_rozdil(1,2,5,3)))
vysledek2 = kalkulacka(2,3 , secti)
print (vysledek2)


