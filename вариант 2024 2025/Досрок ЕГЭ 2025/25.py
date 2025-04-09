def delitel(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    true = [x for x in a if x != 7 and x % 10 == 7]
    return true

for n in range(1125000,1200000):
    if len(delitel(n)) > 0:
        print(n,min(delitel(n)))