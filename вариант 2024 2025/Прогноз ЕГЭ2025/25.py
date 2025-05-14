def delitel(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    a = [f for f in a if f != 134 and f % 1000 == 134]
    return a


for i in range(30000000,32000000):
    if delitel(i):
        print(i,min(delitel(i)))
