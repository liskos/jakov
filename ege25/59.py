def prost_chisla(n):
    a = [True] * 8000000
    a[0] = False
    a[1] = False
    for i in range(2,8000000):
        if a[i]:
            for g in range(i**2,8000000,i):
                a[g] = False
    r = [i for i in range(8000000) if a[i]]
    return r


b = prost_chisla(1)
p = 0
for n in range(7178551,7178659+1):
    if b.count(n):
        p+=1
        print(p,n)

# 1 7178609
# 2 7178617
# 3 7178621
# 4 7178623
# 5 7178627
# 6 7178653
# 7 7178657
# 8 7178659
