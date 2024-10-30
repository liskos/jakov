def f(n):
    b = bin(n)[2:]
    if int(b) % 2 != 0:
        b = b[:-2] + "10"
    else:
        b = "10" + b[2:] + "1"
    return int(b,2)

print(f(4),f(5))
a = []
for i in range(1,1000):
    if i > 25:
        a.append(f(i))

print(min(a))