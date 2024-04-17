def tr(n):
    t = '0123456'
    s = ''
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s

s = tr((7 ** 500 + 7 ** 200 - 7 ** 50 - 1))
print(s)
print(len(s))
print(500*6)

