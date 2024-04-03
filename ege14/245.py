def tr(n):
    t = '01234567'
    s = ''
    while n > 0:
        s = t[n % 8] + s
        n //= 8
    return s

s = 2 ** 102 + 2 ** 100 + 2 ** 85 + 2 ** 17
t = tr(s)
print(set(t))