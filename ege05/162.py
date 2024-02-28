def alg(n):
    b = bin(n)[2:]
    r = b[::-1]
    d = int(r, 2)
    return d


m = 0
for i in range(1, 101):
    result = alg(i)
    if result == 9:
        m = i
print(m)
