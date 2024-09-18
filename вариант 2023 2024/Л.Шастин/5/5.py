def tr(n):
    s = ""
    t = "012"
    while n>0:
        s = t[n%3]+s
        n //= 3
    return s


def f(n):
    b = tr(n)
    if n % 7 == 0:
        b += b[-2:]
    else:
        b += tr((n % 7)*3)
    return int(b,3)

print(f(11),f(14))

a = set()
for i in range(1,1000):
    if f(i) > 369:
        a.add(f(i))
print(min(a))