def tr(n, i):
    t = '0123456789'
    r = ''
    while n > 0:
        r = t[n % i] + r
        n //= i
    return r


for n in range(2, 11):
    if len(set(tr(364, n))) == 1:
        print(n)