def f(n):
    b = bin(n)[2:]
    d = b.count('1')
    b = b + str(d % 2)
    d = b.count('1')
    b = b + str(d % 2)
    return int(b,2)


print(f(13))


m = set()
for i in range(20,51):
    if f(i) > 0:
        m.add(f(i))
print(len(m))
