def d(n):
    t = "0123456789ab"
    s = ""
    while n > 0:
        s = t[n%12]+s
        n //= 12
    return s

def f(n):
    b = d(n)
    if n % 4 == 0:
        b = "2" + b + "64"
    else:
        b += max(x for x in b)
    return int(b,12)

print(f(11),f(12))

a = []
for i in range(1,1000):
    if f(i) > 1799:
        a.append(f(i))
print(min(a))