def alg(n):
    n = bin(n)[2:]
    n += n[-1]
    if n.count('1') % 2 == 0:
        n += n + '0'
    else:
        n += n + '1'
    r = n
    if n.count('1') % 2 == 0:
        r += '11'
    else:
        r += '1'
    return int(r,2)


for i in range(1,1000):
    if alg(i) > 90:
        print(i)
        break