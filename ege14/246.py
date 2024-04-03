def tr(n):
    t = '0123456789abcdef'
    s = ''
    while n > 0:
        s = t[n % 16] + s
        n //= 16
    return s
s = 2 ** 51 + 2 ** 40 + 2 ** 35 + 2 ** 17 - 2 ** 5
t = tr(s)
print(len(set(t)))