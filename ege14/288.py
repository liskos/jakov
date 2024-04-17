def tr(n):
    t = '012345'
    s = ''
    while n > 0:
        s = t[n % 6] + s
        n //= 6
    return s


for x in range(1, 10000):
    s = tr(36 ** 17 - 6 ** x + 71)
    if sum(map(int,s)) == 61:
        print(x)


