def f(n):
    b = bin(n)[2:]
    b = b + str(b.count("1") % 2)
    b = b + str(b.count("1") % 2)
    return int(b,2)


for i in range(1,1000):
    if f(i) > 253:
        print(i)
        break