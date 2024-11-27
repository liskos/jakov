def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += b[-2:]
    else:
        b = "1" + b + "0"
    return int(b,2)

print(f(11),f(10))

for i in range(1,10000):
    if f(i) < 100:
        print(i)