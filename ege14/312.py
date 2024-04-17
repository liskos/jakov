def tr(n):
    t = '0123456'
    s = ''
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


for x in range(1, 10000):
    s = (7 ** 500 + 7 ** 200 - 7 ** 50 - x)
    s = tr(s)
    if int(s) > 0 and x > 0:
        print(sum(map(int,s)))
        break

