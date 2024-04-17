def tr(n):
    t = '0123'
    s = ''
    while n > 0:
        s = t[n % 4] + s
        n //= 4
    return s


for x in range(1, 10000):
    s = (64 ** 11 - 4 ** 10 + 96 - x)
    s = tr(s)
    if sum(map(int,s)) == 71:
        print(x)
        break

