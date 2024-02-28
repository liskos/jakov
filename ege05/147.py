def alg(n):
    n = bin(n)[2:]
    b = n + n[-1]
    if n.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'
    if b.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'
    return int(b, 2)


ar = []
for i in range(1,1000):
    if alg(i) > 105:
        ar.append(alg(i))
print(min(ar))