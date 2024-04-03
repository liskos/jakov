def tr(n):
    t = '01234'
    s = ''
    while n > 0:
        s = t[n % 5] + s
        n //= 5
    return s
s = 5 ** 2004 - 5 ** 1016 - 25 ** 508 - 5 ** 400 + 25 ** 250 - 27
t = tr(s)
print(t.count('4'))
