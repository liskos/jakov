def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = "11" + b[2:] + "0"
    if b.count("1") % 2 != 0:
        b = "10" + b[2:] + "1"
    return int(b,2)


print(f(6))
print(f(4))
for i in range(1,50):
    print(f(i),i)