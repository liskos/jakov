def tr(n):
    s = ""
    t = "012"
    while n > 0:
        s = t[n%3] + s
        n //= 3
    return s

def f(n):
    b = tr(n)
    if n % 3 == 0:
        b += b[:3]
    else:
        b = b + tr(sum(map(int,b)) * 5)
    return int(b,3)
b = []
for i in range(1,500000):
    if f(i) > 2500 and f(i) % 2 != 0:
        b.append(f(i))
print(min(b))