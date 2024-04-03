def tr(n):
    t = '0123456789abcdef'
    s = ''
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s
s = 2 ** 51 + 2 ** 40 + 2 ** 35 + 2 ** 17 - 2 ** 5
t = tr(s)
print(len(set(str(t))))