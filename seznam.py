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
    if i % 2 == 0:
        print(x[i])