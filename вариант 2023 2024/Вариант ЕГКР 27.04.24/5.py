def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b += b[-2]+b[-1]
    else:
        b = b + bin((n % 3) * 3)[2:]
    return int(b,2)

print(f(9),f(10))
a = []
for i in range(1,1000):
    if f(i) > 194:
        a.append(f(i))

print(min(a))