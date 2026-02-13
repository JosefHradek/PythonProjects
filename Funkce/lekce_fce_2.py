
def secti(a, b):
    globalni_promenna = 20
    vysledek = a+b+globalni_promenna # muzem vracet vic veci treba v poli
    return vysledek

def secti_tuple(a, b):
    globalni_promenna = 20
    vysledek = a + b + globalni_promenna  # muzem vracet vic veci treba v poli
    return vysledek, globalni_promenna

globalni_promenna = 10
y = secti (5, 3)
x = secti_tuple(5, 3)
print(type(y))
print(y)
print(globalni_promenna)

print(type(x))
print(x)