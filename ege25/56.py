def prost_chisla(n):
    a = [True] * 7000000
    a[0] = False
    a[1] = False
    for i in range(2,7000000):
        if a[i]:
            for g in range(i**2,7000000,i):
                a[g] = False
    r = [i for i in range(7000000) if a[i]]
    return r


b = prost_chisla(1)
p = 0
for n in range(5962464,5962581+1):
    if b.count(n):
        p+=1
        print(p,n)


# 1 5962477
# 2 5962499
# 3 5962519
# 4 5962547
# 5 5962549
# 6 5962573
# 7 5962577