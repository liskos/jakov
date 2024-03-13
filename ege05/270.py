def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '1' + b + '00'
    else:
        b = '10' + b + '11'
    return int(b,2)
print(f(5))


ar = []
for i in range(1,1000):
    if f(i) > 1023:
        ar.append(f(i))
print(sorted(ar)[0])

