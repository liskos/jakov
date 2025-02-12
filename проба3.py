def delitel(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    if len(a) > 1:
        return max(a)+min(a)
    else:
        return 0


for i in range(800001,1000000):
    if delitel(i) % 10 == 4:
        print(i,delitel(i))