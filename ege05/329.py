def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        r = b +'010'
    else:
        r = b + bin(5 * (n % 3))[2:]
    return int(r,2)


for i in range(1,1000):
    if f(i) > 300 and f(i) % 2 == 0 and f(i) < 315:
        print(i,f(i))