def f(n):
    b = bin(n)[2:]
    c = b[::-1]
    if c.count('0') == 0:
        return 0
    c = c.replace('0','x',1)
    c = c[::-1]
    c = c.replace('x',b[:2] )
    c = c[::-1]
    return int(c,2)


for i in range(2,1000):
    if f(i) == 119:
        print(i)