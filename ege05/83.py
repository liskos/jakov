def alg(n):
    s1 = int(n)
    a = s1//100 + s1//10%10
    b = s1//10%10 + s1%10
    a, b = min(a, b),max(a, b)
    return str(a) + str(b)


f=0
a = []
for i in range(100, 999+1):
    if alg(i) == '1115':
        print(i)
        break




