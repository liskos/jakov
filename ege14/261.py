def tr(n, i):
    t = '0123456789'
    r = ''
    while n > 0:
        r = t[n % i] + r
        n //= i
    return r

a = []
for n in range(2, 11):
    t = tr(7667, n)
    if str(t) == str(t)[::-1]:
        a.append(n)
print(sum(a))
