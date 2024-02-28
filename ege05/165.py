def alg(n):
    b = bin(n)[2:]
    r = b[::-1]
    d = int(r, 2)
    return d


m = 0
for i in range(1,1001):
    result = alg(i)
    if result == 23:
        m = i
print(m)
