def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + b[-3:]
        return int(b,2)
    else:
        b = b + bin(n % 3 * 3)[2:]
        return int(b,2)


for i in range(4,1000):
    if f(i) < 68:
        print(f(i))