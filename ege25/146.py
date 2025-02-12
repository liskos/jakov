def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    chet = [x for x in a if x % 2 == 0]
    netr = min([x for x in a if x != min(a)])
    return len(chet),netr



for n in range(100000000,101000000+1):
    if delitel(n)[0] == 3:
        print(n,delitel(n)[1])