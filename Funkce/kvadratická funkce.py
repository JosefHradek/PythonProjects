def kvadraticka(a,b,c):
    dis = b**2 -4*a*c
    if dis > 0:
        vys_1 = (-b+(dis**(1/2)))/(2*a)
        vys_2 = (-b-(dis**(1/2)))/(2*a)
        return vys_1, vys_2
    elif dis == 0:
        vys = -b/(2*a)
        return vys
    else:
        return "vysledek neni v R"

print(kvadraticka(1, 2,  1))
print(kvadraticka(1, 3,  1))
print(kvadraticka(1, 1,  1))
