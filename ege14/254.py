def tr(n):
    t = '0123456'
    s = ''
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s
s = 43 * 7 ** 103 - 21 * 7 ** 57 + 98
t = tr(s)
b = sum(map(int,t))
b = str(b)
print(b)
