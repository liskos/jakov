def tr(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]

def f(n):
    s = tr(n)
    if n % 2 == 0:
        s += s[-2:]
    else:
        n = sum(map(int,s))
        s += tr(n)
    return int(s,3)


print(f(10))
print(f(11))

for i in range(10,100000):
    if f(i) == 82:
        print(i, f(i))

