def tr(n):
    t = '01234'
    s = ''
    while n > 0:
        s = t[n % 5] + s
        n //= 5
    return s
s = 5 ** 94 + 25 ** 49 - 130
t = tr(s)
print(t.count('4'))
