def tr(n):
    t = '0123456789abc'
    s = ''
    while n > 0:
        s = t[n % 13] + s
        n //= 13
    return s


s = 26 ** 2 + 169 - 11
t = tr(s)
print(t.count('c'),t.count('2'))
