def f(n):
    n = bin(n)[2:]
    c = sum(map(int, n))
    if c % 2 == 0:
        n += '1'
    else:
        n += '0'
    b = sum(map(int, n))
    if b % 2 == 0:
        n += '1'
    else:
        n += '0'
    return int(n, 2)


m = set()
for i in range(1, 100):
    r = f(i)
    if 16 <= r <= 32:
        m.add(r)
print(len(m))
