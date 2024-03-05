def alg(n):
    n = bin(n)[2:]
    b = n.replace("0","")
    return int(b,2)


m = set()
for i in range(10,2501):
    if alg(i) == alg(i):
        m.add(alg(i))
print(len(m))


