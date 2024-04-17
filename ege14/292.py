def tr(n):
    t = '012'
    s = ''
    while n > 0:
        s = t[n % 3] + s
        n //= 3
    return s


for x in range(1, 10000):
    s = (27 ** 7 - 3 ** 11 + 36 - x)
    s = tr(s)
    if sum(map(int,s)) == 22:
        print(x)
        break

