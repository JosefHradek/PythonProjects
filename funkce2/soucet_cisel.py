def soucet(n):
    souc = 0
    for i in range(n+1):
        souc = souc + i

    return souc

print(soucet(6))


def soucet2(n):
    if n <= 0:
        return 0
    else:
        return n + soucet2(n-1)


print(soucet2(5))