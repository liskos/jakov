def tr(n):
    t = '0123456789abcdef'
    s = ''
    while n > 0:
        s = t[n % 16] + s
        n //= 16
    return s


s = 15 + 2 ** 10 + 16
t = tr(s)
print(t.count('f'))
