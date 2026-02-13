promenna = [1, 2, 3, 4, 5]

print(promenna)

p2 = [1, "abc", 5.5, True, [1,2,"a"]]
print(p2)

print(p2[4])
print(type(p2[4][1]))
print(type(p2))
print(p2[4][1])
print(p2[1:4])

x = [1, 2, 8, 4, 6, 11, 7, 4]

for i in range(len(x)):
    if i % 2 > 0:
        print(x[i])

print("pr 2*************************")

for i in range(len(x)):
    if i % 2 == 0:
        print(x[i])

print("14.11.2025")
print("pr1")

pole = [20, 2, 9, 1, 7, 3, 10, 6, 4]
#hledani maximalniho prvku a pozice
maximum = pole[0]
pozice_max = 0

for i in range(len(pole)):
    if maximum < pole[i]:
        maximum = pole[i]
        pozice_max = i

print(maximum,pozice_max)

print("pr2")
pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]

minimum = pole[0]
min_poz = 0

for i in range(len(pole)):
    if minimum > pole[i]:
        minimum = pole[i]
        min_poz = i

print(minimum, min_poz)

print("pr3")

citatel = 0
jmenovatel = len(pole)


for i in range(len(pole)):
    citatel += pole[i]

vysledek = citatel/jmenovatel
print(vysledek)

print("pr4")

pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]

limit = 5
pocet_cisel = 0

for i in range(len(pole)):
    if pole[i] > limit:
        pocet_cisel += 1

print("pocet cisel vetsich nez "+ str(limit)+" je "+str(pocet_cisel)+".")

print("pr5")

pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]

soucet = 0

for i in range(len(pole)):
    soucet += pole[i]

print(soucet)

print("pr6")

pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]
nove_pole = []

for i in range(len(pole)-1,-1,-1):
    nove_pole.append(pole[i])

print(nove_pole)

print("pr7")

pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]
pole2 = [3, 5, 4, 7, 5, 3, 4, 5, 10]
nove_pole = []


for i in range(len(pole)):
    nove_pole.append(pole[i] + pole2[i])

print(nove_pole)

print("pr8")

pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]
pole2 = [3, 5, 4, 7, 5, 3, 4, 5, 10]
nove_pole = []


for i in range(len(pole)):
    nove_pole.append(pole[i] + pole2[-i-1])

print(nove_pole)

print("pr9")

druhy_prvek = -10000000                 #float('-inf')
prvni_prvek = -10000000             #float('-inf')

pole = [2, 2, 9, 1, 7, 3, 6, 7, 4]

for i in range (len(pole)):
    if pole[i] > prvni_prvek:
        druhy_prvek = prvni_prvek
        prvni_prvek = pole[i]
    elif pole[i] > druhy_prvek:
        druhy_prvek = pole[i]

print(druhy_prvek)
print(prvni_prvek)

print("pr10")

pole = [2, 2, 9, 1, 7, 3, 6, 7, 4]
je = True
for i in range(len(pole)):
    if pole[i] > pole[i+1]:
        je = False
        break
if je:     # =if je == True
    print(je)
else:           # =elif je == False
    print(je)
print("pr_bonus")

pole = [2, 2, 4, 1, 7, 3, 6, 7, 4]
pocet_sudych = 0
lichy = 0
for i in range(len(pole)):
    if pole[i]%2 == 0:
        pocet_sudych += 1
    else:
        lichy += 1
print(pocet_sudych,",",lichy)

print("pr11")

