def f(n):
    b = bin(n)[2:]
    if n % 5 == 0:
        b = b[:3] + b
    else:
        b += bin((n % 5)*5)[2:]
    return int(b,2)

print(f(12))

for i in range(1,10000):
    if f(i) < 313 and i % 2 != 0:
        print(i)