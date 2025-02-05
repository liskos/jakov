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
for n in range(5408238,5408389+1):
    if b.count(n):
        p+=1
        print(p,n)

# 1 5408309
# 2 5408311
# 3 5408323
# 4 5408341
# 5 5408357
# 6 5408383
# 7 5408387