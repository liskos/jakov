def f(n):
    b = bin(n)[2:]
    if b.count("1") % 3 == 0:
        b += bin(sum(map(int,b))%5)[2:]
    else:
        b = "1" + b + "10"

    return int(b,2)
b = []
print(f(5),f(7))
for i in range(1,1000):
    if f(i) > 89:
        b.append(f(i))

print(min(b))