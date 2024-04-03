def tr(n):
    t = '0123456789abcde'
    s = ''
    while n > 0:
        s = t[n % 15] + s
        n //= 15
    return s


s = 100 ** 2 + 625 ** 25 + 5 ** 100
t = tr(s)
print(t.count('c'))
