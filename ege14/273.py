def tr(n):
    t = '0123456789abcd'
    s = ''
    while n > 0:
        s = t[n % 14] + s
        n //= 14
    return s


s = 7 ** 2 + 49 ** 4 - 21
t = tr(s)
print(t.count('a'),t.count('0'))
