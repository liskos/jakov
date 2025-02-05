def prost(n):
    a = [True] * 5000000
    a[0] = False
    a[1] = False
    for i in range(2,5000000):
        if a[i]:
            for g in range(i**2,5000000,i):
                a[g] = False
    r = [i for i in range(5000000)if a[i]]
    return r

b = prost(1)
p = 0
for n in range(2484292,2484371):
    if b.count(n):
        p += 1
        print(p,n)

# 1 2484311
# 2 2484319
# 3 2484323
# 4 2484331
# 5 2484353
# 6 2484359