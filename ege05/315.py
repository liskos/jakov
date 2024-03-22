def f(n):
    b = bin(n)[2:]
    if n % 3:
        b = b + b[-3] + b[-2] + b[-1]
        return int(b,2)
    else:
        b = n % 3 * 3
        return b

for i in range(8,1000):
    if f(i) >= 120:
        print(i)