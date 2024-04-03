def tr(n):
    s = '0123'
    r = ''
    while n > 0:
        r = s[n % 4] + r
        n //= 4
    return r


a = []
for x in range(1,50):
    for y in range(1,50):
        s = (3 + 2 * 4 ** x) * 4 ** x + 3 + 4 ** y
        t = tr(s)
        a.append(sum(map(int,t)))
print(max(a))