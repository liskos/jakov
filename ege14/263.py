def tr(n, i):
    t = '0123456789'
    r = ''
    while n > 0:
        r = t[n % i] + r
        n //= i
    return r

def f(n):
    n = str(n)
    for i in range(len(n)-1):
        if n[i] > n[i + 1]:
            return False
    return True



b = []
for n in range(2, 11):
    t = tr(188, n)
    if f(t):
        b.append(n)
print(sum(b))