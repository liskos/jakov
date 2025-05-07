
def delitel(n):
    a = set()

    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sum(a)
print(delitel(20))

for n in range(500001,1000000):
    if delitel(n) % 10 == 6:
        print(n,delitel(n))