import numpy as np

for i in range(10):
    cislo = np.random.randint(10,20)
    print(cislo)
    rnd = np.random.random()
    print(rnd)
#<>
print("hra")
nahodne_cislo = np.random.randint(21)
while True:
    while True:
        h_cislo = input("hadej cislo: ")
        try:
            cislo = int(h_cislo)
            break
        except:
            pass
    if cislo == nahodne_cislo:
        break
    elif cislo > nahodne_cislo:
        print("hledane cislo je mensi")
        pass
    elif cislo < nahodne_cislo:
        print("hledane cislo je vetsi")
        pass
print("super spravne")
