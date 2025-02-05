def prost(n):
    a = [True] * 5000000
    a[0] = False
    a[1] = False
    for i in range(2,5000000):
        if a[i]:
            for g in range(i**2,5000000,i):
                a[g] = False
    r = [i for i in range(5000000) if a[i]]
    return r


b = prost(5)
p = 0
for n in range(4837177,4837237):
    if b.count(n):
        p += 1
        print(p,n)

# 1 4837187
# 2 4837201
# 3 4837213
# 4 4837219
# 5 4837223