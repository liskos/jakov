def f(n):
    b = bin(n)[2:]
    if b.count("1")%2 == 0:
        b = "10" + b[2:]+ "0"
    else:
        b = "11" + b[2:] + "1"
    return int(b,2)

print(f(6),f(4))
a = []
for i in range(1,1000):
    if i > 27:
        a.append(f(i))
print(min(a))