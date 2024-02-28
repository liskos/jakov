def f(n):
    n = bin(n)[2:]
    n += n[-1]
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    return int(n,2)


ar = []
for i in range(1,10000):
    if f(i) > 130:
        ar.append(i)
print(min(ar))
