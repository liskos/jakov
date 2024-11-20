def f(n):
    b = bin(n)[2:]
    if int(b) % 2 == 0:
        b = "10" + b
    else:
        b = "1" + b + "01"
    return int(b,2)

print(f(4),f(5))


for i in range(1,1000):
    if f(i) > 516:
        print(i)