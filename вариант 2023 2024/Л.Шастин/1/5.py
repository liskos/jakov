def tr(n):
    s = '012'
    r = ''
    while n > 0:
         r = s[n % 3] + r
         n //= 3
    return r


def g(n):
    t = tr(n)
    if n % 3 == 0:
        t = t + t[:2]
    else:
        t = t + tr(n % 3 * 5)
    return int(t,3)


a = []
print(g(11), g(12))
for i in range(3,1000):
    if g(i) > 64:
        a.append(g(i))
print(min(a))

