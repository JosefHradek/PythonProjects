

a = 5
def max_2(s):
    if s[0] > s[1]:
        maxim = s[0]
        max2 = s[1]
    else:
        maxim = s[1]
        max2 = s[0]
    for i in range(len(s)):
        if s[i] > maxim:
            max2 = maxim
            maxim = s[i]
        if s[i] > max2 and s[i] < maxim:
            max2 = s[i]
    return max2

seznam = [10,5,7,8,19,2,10,2,15,2,19]
print((a-1)*" " + str(max_2(seznam)))

for i in range (a):
    print((a-i)*" "+i*"/"+i*"\\"+(a-i)*" ")
for i in range(round(a/2)):
    print((a-1)*" "+"||"+(a-1)*" ")

def prvo(a):
    for i in range (2,a):
        if a%(i) == 0:
            return False
    return True

print(prvo(13))

