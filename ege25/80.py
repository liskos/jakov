def prost(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2,n):
        if a[i]:
            for g in range(i**2,n,i):
                a[g] = False
    r = [i for i in range(n) if a[i]]
    return r

a = 0
b = prost(10000001)
for i in range(2,10000000+1):
    k = 0
    for x in b:
        if i % x == 0:
            k += 1
        if x > i:
            break
    a = max(a,k)

print(a)