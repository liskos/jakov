def prost(n):
    a = [True] * 4000000
    a[0] = False
    a[1] = False
    for i in range(2,4000000):
        if a[i]:
            for g in range(i**2,4000000,i):
                a[g] = False
    r = [i for i in range(4000000) if a[i]]
    return r
b = prost(1)
def delitel(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    x = [x for x in a if b.count(x)]
    return max(x) - min(x)


for i in range(3333337,4000000):
    if delitel(i) > 1000 and delitel(i) % 3 == 0:
        print(i,delitel(i))