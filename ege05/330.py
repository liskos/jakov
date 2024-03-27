def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        n = b + b[-3:]
    else:
        n = b + bin((n % 3)*3)[2:]
    return int(n,2)


for i in range(1,1000):
    if f(i) < 170:
        print(f(i))