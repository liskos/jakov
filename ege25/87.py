def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a

b = [x**2 for x in range(2,136)]
k = 0
for n in range(2945,18294+1):
    divs = delitel(n)
    c = [x for x in b if n % x == 0]
    if not c:
        k += sum(map(int,str(n)))

print(k)
