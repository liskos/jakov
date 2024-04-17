def tr(n):
    t = '012345678'
    s = ''
    while n > 0:
        s = t[n % 9] + s
        n //= 9
    return s


for x in range(1, 10000):
    s = (81 ** 20 - 9 ** x + 50)
    s = tr(s)
    if sum(map(int,s)) == 138:
        print(x)


