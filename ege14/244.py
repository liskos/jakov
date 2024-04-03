def tr(n):
    t = '0123456'
    s = ''
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s
s = (7 ** (9 ** 2 - 1) - (10 - 3) ** 4 ) * 20 // 3
t = tr(s)
print(t.count('4'))
