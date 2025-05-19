def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = "1" + b[:-2] + "11"
    else:
        b = "10" + b + "0"

    return int(b,2)

print(f(4),f(6))

b = []
for i in range(1,10000):
    if f(i) > 999 and i % 2 == 0:
        b.append(f(i))

print(min(b))