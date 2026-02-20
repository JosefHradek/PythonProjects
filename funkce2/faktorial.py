def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


def odpocet(n):
    if n == 0:
        return "boom"
    else:
        print("odpocet T - " + str(n))
        return odpocet(n-1)

print(odpocet(5))
