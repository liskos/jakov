def f(n):
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    return int(n, 2)


m = set()
for i in range(1, 1000):
    if 16 <= f(i) <= 32:
        m.add(f(i))
print(len(range(16, 33)) - len(m))
