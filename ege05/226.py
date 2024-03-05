def f(n):
    n = bin(n)[2:]
    b = str(n)
    n = str(n) + b[-2]
    n = str(n) + b[1]
    return int(n, 2)


print(f(11))
for i in range(10,100):
    if f(i) < 128:
        print(i)