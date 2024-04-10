def tr(n, i):
    t = '0123456789'
    r = ''
    while n > 0:
        r = t[n % i] + r
        n //= i
    return r


def f(t):
    for i in range(len(t) - 1):
        if t[i] == t[i+1]:
            return True
    return False

for n in range(2, 11):
    t = tr(572, n)
    if f(t):
        print(n)
