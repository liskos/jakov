def f(n):
    b = bin(n)[2:]
    if n % 5:
        b = b + b[-3] + b[-2] + b[-1]
        return int(b,2)
    else:
        b = n % 5 * 5
        return b


for i in range(4,1000):
    if f(i) < 100:
        print(i)