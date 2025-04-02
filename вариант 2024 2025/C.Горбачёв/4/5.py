def f(n):
    b = bin(n)[2:]
    if len(b) % 2 == 0:
        b += "1"
    else:
        b = "1" + b + "0"
    return int(b,2)

b = []
for i in range(1,1000):
    if f(i) > 666:
        b.append(f(i))


print(min(b))