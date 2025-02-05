def prost(n):
    a = [True] * 4000000
    a[0] = False
    a[1] = False
    for i in range(2,4000000):
        if a[i]:
            for g in range(i**2,4000000,i):
                a[g] = False
    r = [i for i in range(4000000) if a[i]]
    return r


k = 0
b = prost(1)
for n in range(2,20000+1):
    if b.count(n):
        k += 1


print(k)

#2262