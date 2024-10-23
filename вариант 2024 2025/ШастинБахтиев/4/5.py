a = []


def f(n):
    b = bin(n)[2:]
    if len(b) % 2 == 0:
        b += "1"
    else:
        b = "1" + b + "0"
    return int(b,2)

print(f(3))

for i in range(1,10000):
    if f(i) > 666:
        a.append(f(i))
print(min(a))