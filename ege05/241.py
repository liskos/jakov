def f(n):
    b = bin(n)[2:]
    b = '0' * (8 - len(b)) + b
    c = b[::-1]
    return int(b,2) - int(c,2)


ar = []
for i in range(1,256):
    if f(i) > 0:
        ar.append(f(i))
print(ar[-1])

