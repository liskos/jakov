def prost_chisla(n):
    a = [True] * 1000000
    a[0] = False
    a[1] = False
    for i in range(2,1000000):
        if a[i]:
            for g in range(i**2,1000000,i):
                a[g] = False
    r = [i for i in range(1000000) if a[i]]
    return r

print(prost_chisla(1005))