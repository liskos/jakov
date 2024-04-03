def tr(n):
    s = '01234'
    r = ''
    while n > 0:
        r = s[n % 5] + r
        n //= 5
    return r


a = []
for x in range(1,50):
    for y in range(1,50):
        s = (55 + 2 * 5 ** x) * 5 ** x + 55 + 5 ** y
        t = tr(s)
        a.append(sum(map(int,t)))
print(max(a))