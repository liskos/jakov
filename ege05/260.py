def f(n):
    b = bin(n)[2:]
    c = b[:2]
    if b.count('0') == 0:
        return 0
    b = b[::-1]
    b = b.replace('0','x',1)
    b = b[::-1]
    b = b.replace('x',c)
    b = b[::-1]
    return int(b,2)

for i in range(2,1000):
    if f(i) == 123:
        print(i)