text = "ahoj"
text2 = 'ahooj'
text3 = " Sean O'Connery"
text4 = 'tak řekl "blablabla..." a tak dal'
text5 = 'Sean O\'Connery' #text7 = "tak řekl \"blablabla...\" a tak dal"
text6 = " cesta k souboru je c:\\hry\\soubor.txt"
text7 = "ahoj \n nazdar"
#string retezec znaku

##print(text7)

a = "abc"
b = "def"
print(a*3)

c = "a"
for i in range(5):
    c += "a"

print(c)

promenna = "Ahoj Karle, jak sem máš?"

print(promenna[6]) #vypise pismeno na nadem míste v tomto pripade {[(6)]} :) (zacina od 0) (mezera je jako pismeno)

print(len(promenna))

for i in range (len(promenna)): # to "len" mi spocita pocet pismen v promenny takze je jako cislo  ve smycce
    print(promenna[i])

print(promenna[len(promenna)-1])

print(promenna[5:10])

print(promenna[5:10:2])

print(promenna[10:5:-2])

print(promenna[5:])

print(promenna[:5])

print(promenna[:5:-1])

print(promenna[5::-1])

print(promenna[::-1])

print(promenna.index(",")) #spotuje kde je dany znak