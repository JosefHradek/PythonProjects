import numpy as np

for i in range(10):
    cislo = np.random.randint(10,20)
    print(cislo)
    rnd = np.random.random()
    print(rnd)
#<>
print("hádací hra")
nahodne_cislo = np.random.randint(1,21)
pocet_pokusu = 0
pocet_inva_pokusu = 0
while True:
    while True:
        h_cislo = input("hadej cislo od 1 do 20: ")
        try:
            cislo = int(h_cislo)
            break
        except:
            print("nepises cislo")
            pass
    if cislo > 0 and cislo < 21:
        pocet_inva_pokusu += 1
        pocet_pokusu += 1
        if cislo == nahodne_cislo:
            break
        elif cislo > nahodne_cislo:
            print("hledane cislo je mensi")
            pass
        elif cislo < nahodne_cislo:
            print("hledane cislo je vetsi")
            pass
    else:
        pocet_inva_pokusu += 1
        print ("zkus znova cislo mimo interval")


print("super spravne")
print("počet validních pokusů je: " + str(pocet_pokusu))
print("počet invalidních pokusů je: " + str(pocet_inva_pokusu))
if pocet_pokusu == 1:
    print("tybrdo 1 pokus vyhravas zlatyho bludistaka")
elif pocet_pokusu > 1 & pocet_pokusu < 6:
    print ("no dobry")
else:
    print("nic moc typku")


