
def delitel(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a
def f(n):
    d = delitel(n)
    return max(d) - min(d) if d else 0

for n in range(1526464,1533879):
    d = f(n)
    if d > 5000 and d % 1235 == 0:
        print(n,d)


