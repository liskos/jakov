def tr(n):
    t = '01234567'
    s = ''
    while n > 0:
        s = t[n % 8] + s
        n //= 8
    return s
s = (2 ** 345 + 8 ** 65 - 4 ** 130)*(8 ** 123 - 2 ** 89 + 4 ** 45)
t = tr(s)
print(sum(map(int,t)))