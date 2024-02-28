def alg(n):
    b = bin(n)[2:]
    r = b[::-1]
    d = int(r, 2)
    return d


m = 0
for i in range(1000,5000):
    result = alg(i)
    if result == 29:
        print(result)
        break
