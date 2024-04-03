def tr(n):
    s = '01234567'
    r = ''
    while n > 0:
        r = s[n % 8] + r
        n //= 8
    return r


for x in range(4,11):
    s = (88 + 2 * 8 ** x)*8**x + 88 + 8 ** 8
    t = tr(s)
    print(t, sum(map(int,t)))
