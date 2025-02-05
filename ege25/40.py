def prost_chisla(n):
    a = [True] * 20000000
    a[0] = False
    a[1] = False
    for i in range(2,20000000):
        if a[i]:
            for g in range(i**2,20000000,i):
                a[g] = False
    r = [i for i in range(20000000) if a[i]]
    return r
b = prost_chisla(1)
for n in range(2943444,2943530):
    if b.count(n):
        print(n)


#1 2943467
#2 2943491
#3 2943503
#4 2943527