def tr(n):
    s = ""
    t = "012"
    while n>0:
        s = t[n%3]+s
        n //= 3
    return s

def f(n):
    b = tr(n)
    if n % 3 == 0:
        b+= b[-2:]
    else:
        b = b + tr(sum(map(int,b)))
    return int(b,3)

print(f(11),f(12))

a = []
for i in range(1,100000):
    if 220 < f(i) and f(i) % 2 == 0:
        a.append(f(i))
print(min(a))