def f(n):
    b = bin(n)[2:]
    d = b.count('1')
    b = b + str(d % 2)
    d = b.count('1')
    b = b + str(d % 2)
    return int(b,2)


print(f(13))


m = set()
for i in range(1,10000):
    if 20 <= f(i) <= 50:
        m.add(f(i))
print(len(m))
