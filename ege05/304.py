def f(n):
    n = hex(n)[2:]
    if n % 2 == 0:
        n += 'F'
    else:
        n += '0'
    n += hex(sum(map(int,n)))[2:] % 16
    n += hex(sum(map(int,n)))[2:] % 16
    return int(n,16)


for i in range(1,1000):
    if 