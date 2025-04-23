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
        b = b + b[-2:]
    else:
        b = b + tr(n//3*3)
    return int(b,3)

print(f(6),f(4))

for i in range(2,1000):
    if f(i) < 151:
        print(i)