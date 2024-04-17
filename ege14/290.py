def tr(n):
    t = '01234567'
    s = ''
    while n > 0:
        s = t[n % 8] + s
        n //= 8
    return s


for x in range(1, 10000):
    s = (64 ** 12 - 8 ** 14 + x)
    s = tr(s)
    if s.count("7")== 12 and s.count('1') == 1:
        print(x)
        break

