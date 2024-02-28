def f(n):
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        a = '0'
    else:
        a = '1'
    r = n + a
    if r.count('1') % 2 == 0:
        b = '0'
    else:
        b = '1'
    r+=b
    return int(r,2)


for i in range(1,10000):
    if f(i)<125:
        print(f(i))