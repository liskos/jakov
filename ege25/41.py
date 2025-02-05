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
c = 0
for n in range(4671032,4671106):
    if b.count(n):
        c = c + 1
        print(c,n)

# 1 4671071
# 2 4671077
# 3 4671097
# 4 4671101