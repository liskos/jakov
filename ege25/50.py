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


b = prost(1)
p = 0

for n in range(2532421,2532492):
    if b.count(n):
        p+=1
        print(p,n)

# 1 2532433
# 2 2532437
# 3 2532449
# 4 2532451
# 5 2532479
# 6 2532487