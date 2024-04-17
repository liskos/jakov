def tr(n):
    t = '01234'
    s = ''
    while n > 0:
        s = t[n % 5] + s
        n //= 5
    return s


for x in range(1, 10000):
    s = (125 ** 7 - 25 ** 4 + x)
    s = tr(s)
    if s.count("4")== 15 and s.count('3')== 1 and s.count('1') == 2:
        print(x)
        break

