def prost(n):
    a = [True] * 7000000
    a[0] = False
    a[1] = True
    for i in range(2,7000000):
        if a[i]:
            for g in range(i**2,7000000,i):
                a[g] = False
    r = [i for i in range(7000000) if a[i]]
    return r

b = prost(1)
p = 0

for n in range(6638225,6638322+1):
    if b.count(n):
        p+=1
        print(p,n)

# 1 6638227
# 2 6638231
# 3 6638249
# 4 6638251
# 5 6638263
# 6 6638273
# 7 6638299
# 8 6638321