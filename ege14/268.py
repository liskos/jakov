def tr(n, i):
    t = '0123456789'
    r = ''
    while n > 0:
        r = t[n % i] + r
        n //= 10
    return r


for n in range(2, 11):
    t = tr(572, n)
    s, s2, s3 = str(t)
    print(s, s2, s3, n)

2 + 4 + 5