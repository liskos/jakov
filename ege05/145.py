def alg(n):
    n = bin(n)[2:]
    n = n + n[-1]
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    r = n
    if r.count('1') % 2 == 0:
        r += '11'
    else:
        r += '1'
    return int(n,2)


for i in range(1,1000):
    if alg(i) > 80:
        print(alg(i))
        break
