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
for n in range(6080068,6080176+1):
    if b.count(n):
        p+=1
        print(p,n)

# 1 6080069
# 2 6080131
# 3 6080141
# 4 6080147
# 5 6080149
# 6 6080153
# 7 6080161