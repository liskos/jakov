def tr(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]

def f(n):
    t = tr(n)
    if n % 3 == 0:
        t += t[-2:]
    else:
        t += tr(n % 3 * 5)
    return int(t,3)

print(f(11), f(12))
for i in range(1,1000):
    if 150>f(i) > 133:
        print(f(i))