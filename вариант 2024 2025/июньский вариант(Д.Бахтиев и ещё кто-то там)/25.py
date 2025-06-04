def prost(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2,n):
        if a[i]:
            for g in range(i**2,n,i):
                a[g] = False
    r = [i for i in range(n) if a[i]]
    return r
pr = prost(1000000)
def delitel(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    b = [x for x in a if pr.count(x)]
    b = sorted(b)
    if len(b) < 4:
        return 0
    return b[0] + b[1] + b[-1] + b[-2]

for i in range(456790,1000000):
    if delitel(i) % 114 == 39:
        print(i,delitel(i))