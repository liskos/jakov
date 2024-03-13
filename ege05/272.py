def f(n):
    n = n // 2
    b = hex(n)[2:]
    if n % 4 == 0:
        b = '15' + b + 'C'
    else:
        b = 'F' + b + 'AO'
    return int(b,16)
print(f(45))


ar = []
for i in range(1,1000):
    if f(i) > 1000:
        ar.append(f(i))
print(sorted(ar)[0])

