def prost(n):
    a = [True] * 1000000
    a[0] = False
    a[1] = False
    for i in range(2,1000000):
        if a[i]:
            for g in range(i**2,1000000,i):
                a[g] = False
    r = [i for i in range(1000000) if a[i]]
    return r


b = prost(1)
k = 0
for n in range(2948,20194+1):
    if b.count(n):
        print(n)


#20183