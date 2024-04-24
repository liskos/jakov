def tr(n):
    t = '0123456'
    s = ''
    while n > 0:
        s = t[n%7] + s
        n //= 7
    return s

b = int('234',7)
s = (7**80 - (7)**4 + b) * 5//3 * 4
t = tr(s)
print(t.count('4'))