def prost(n):
    a = [True] * 5000000
    a[0] = False
    a[1] = False
    for i in range(2,5000000):
        if a[i]:
            for g in range(i**2,5000000,i):
                a[g] = False
    r = [i for i in range(5000000) if a[i]]
    return r


b = prost(1)
k = 0

for d in b:
    if 1 < d < 3577001:
        k += 1

print(k)


#255203