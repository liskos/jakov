def f(n):
    b = bin(n)[2:]
    b += str(int(b.count("1"))%2)
    b += str(int(b.count("1"))%2)
    return int(b,2)

for i in range(1,10000):
    if f(i) > 123:
        print(f(i))