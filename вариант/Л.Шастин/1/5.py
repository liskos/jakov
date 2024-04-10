def tr(n):
    s = '012'
    r = ''
    while n > 0:
         r = s[n % 3] + r
         n //= 3
    return r
def g(j):
    h = tr(j)
    if j % 3 == 0:
        j = str(j) + h[0] + h[1]
    else:
        j = str(j) + tr(j % 3 * 5)
    return int(j,3)


for i in range(3,1000):
    if g(i) > 64:
        print(g(i))

