def tr(n,i):
    t = '0123456789'
    r = ''
    while n > 0:
        r = t[n % i] + r
        n //= i
    return r

def f(t):
    t = str(t)
    return int(t[0]) % 2 != int(t[-1]) % 2

a = []
for n in range(2,11):
    t = tr(609,n)
    if f(t):
        a.append(n)
print(sum(a))

