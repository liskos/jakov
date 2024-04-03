def tr(n):
    t = '0123456'
    s = ''
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s
s = 5 ** 2 * 7 ** 25 + 6 ** 2 * 7 ** 36 - 4 ** 2 * 9 ** 3
t = tr(s)
print(t.count('0'))
