def tr(n):
    t = '0123456'
    s = ''
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s
s = 7 ** 202 + 49 ** 102 - 7 ** 20
t = tr(s)
print(t.count('6'))
