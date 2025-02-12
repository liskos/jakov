def prost(n):
    a = [True] * 100000
    a[0] = False
    a[1] = False
    for i in range(2,100000):
        if a[i]:
            for g in range(i**2,100000,i):
                a[g] = False
    r = [i for i in range(100000) if a[i]]
    return r
b = prost(1)
def delitel(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    a = sum([x for x in a if b.count(x)])
    return a


for n in range(33333,55555+1):
    if delitel(n) != 0:
        if (n % delitel(n) == 0) and (delitel(n) > 250):
            print(n,delitel(n))

# 38086 278
# 44998 302
# 53332 268
