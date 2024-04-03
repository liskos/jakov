def tr(n):
    t = '0123456789abcdefg'
    s = ''
    while n > 0:
        s = t[n % 17] + s
        n //= 17
    return s


s = 17 ** 5 + 85 ** 8 - 10
t = tr(s)
print(t.count('g'))
