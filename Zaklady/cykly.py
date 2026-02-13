for i in range(6): #opakuje se dokud neskonci cyklus
       print(i*2)

for i in range(0, 11):
    if i%2 == 0:
        print(i)
    else:
        print("nope")

for i in range(5):
    for j in range(5):
        print(str(i) + ", " + str(j))

a = 0
while a == 0:
    x = input("napis cislo: ")
    try:
        a = int(x)
    except:
        a = 0

print(a)


for i in range(10):
    print(i)
    if i > 5:
        continue #ukonci smicku a skoci nazacatek
    print("ahoj")

for i in range(10):
    print(i)
    if i > 5:
         break # okamzite ukonci smycku nezacina od zacatku
    print("ahoj")


while True:
    x = input("napis cislo: ")
    try:
        a = int(x)
        break
    except:
        pass
print(a)


