while True:
    cislo_jako_text = input("Zadej cislo: ")
    try:
        cislo = int(cislo_jako_text)
        break
    except:
        print("blbe")
        pass


print("cislo + 10 je " + str(cislo + 10))