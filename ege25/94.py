def prosto(n):
    a = [True] * 100000
    a[0] = False
    a[1] = False
    for i in range(2,100000):
        if a[i]:
            for g in range(i**2,100000,i):
                a[g] = True
    r = [i for i in range(100000)if a[i]]
    return r


b = prosto(1)
k = 0
for n in range(3159,31584+1):
    if b.count(n):
        k += sum(map(int,str(n)))
print(k)

#550113
