def f(n):
    n = bin(n)[2:]
    b = n[:-2]
    return int(b, 2)


m = set()
for i in range(20,601):
    if f(i) == f(i):
        m.add(f(i))
print(len(m))

