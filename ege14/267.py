def tr(n, i):
    t = '0123456789'
    r = ''
    while n > 0:
        r = t[n % i] + r
        n //= i
    return r

a = []
for n in range(2, 11):
    t = tr(652, n)
    if '2' not in t:
        a.append(n)
print(sum(a))

