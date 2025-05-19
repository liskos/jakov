def delitel(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    if not a:
        return 0
    m = min(a) + max(a)
    return m


for n in range(900000,1000000):
    if delitel(n) % 100 == 46:
        print(n,delitel(n))