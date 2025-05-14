def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = "10" + b + "0"
    else:
        b = "1" + b + "11"

    return int(b,2)

print(f(4),f(5))
d = []
for i in range(1,10000):
    if f(i) < 410:
        d.append(f(i))

print(max(d))