def delitel(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sum(a)


print(delitel(20))
for i in range(500001,900001):
    if delitel(i) % 10 == 9:
        print(i,(delitel(i)))