def tr(n):
    t = '0123456789abcdef'
    s = ''
    while n > 0:
        s = t[n % 16] + s
        n //= 16
    return s


s = 256 ** 2 + 4096 ** 16 - 15
t = tr(s)
print(t.count('f'))
