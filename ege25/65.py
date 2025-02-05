def prost(chisla):
    a = [True] * 3000000
    a[0] = False
    a[1] = False
    for i in range(2,3000000):
        if a[i]:
            for g in range(i**2,3000000,i):
                a[g] = False
    r = [i for i in range(3000000) if a[i]]
    return r


b = prost(1)
p = 0
d = []

for n in range(2532000,2532160+1):
    if b.count(n):
        d.append(n)

for h in d:
    p += 1
    if p % 3 == 1 or p == 1:
        print(p,h)
# 1 2532007
# 4 2532083
# 7 2532113
# 10 2532157