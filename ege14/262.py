def tr(n, i):
    t = '0123456789'
    r = []
    while n > 0:
        r.append(t[n % i])
        n //= i
    return r[::-1]

def f(a):
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            return False
    return True

b = []
for n in range(2, 11):
    t = tr(432, n)
    if f(t):
        b.append(n)
print(sum(b))
