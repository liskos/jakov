def alg(n):
    s1 = int(n)
    a = s1//1000 + s1//100%10
    b = s1//10%10 + s1%10
    a, b = min(a, b),max(a, b)
    return str(a) + str(b)


f=0
a = []
for i in range(1000, 9999+1):
    if alg(i) == '117':
        f=i
print(f)



