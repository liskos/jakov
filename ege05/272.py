def f(n):
    b = hex(n // 2)[2:]
    if n % 4 == 0:
        b = 'ege15' + b + 'C'
    else:
        b = 'F' + b + 'A0'
    return int(b,16)
print(f(4))


ar = []
for i in range(1,10000):
    if f(i) < 65536:
        ar.append(i)
print(max(ar))

