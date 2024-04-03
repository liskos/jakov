def tr9(n):
    s = '012345678'
    r = ''
    while n > 0:
        r = s[n % 9] + r
        n //= 9
    return r

for x in range(1,1000):
    t9 = tr9(x)
    t3 = tr9(x * 3)
    if (len(t9) == 3) and ('3' in t9) and (len(t3) == 3):
        print(x)
print(tr9(84 + 237))