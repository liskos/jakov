def f(n):
    b = bin(n)[2:]
    if n % 7 == 0:
        b = b + bin(7)[2:]
    else:
        b = b + '1'
    if int(b, 2) % 5 == 0:
        b += bin(5)[2:]
    else:
        b += '1'
    return int(b, 2)

for i in range(1,1000000):
    if f(i) > 500000:
        print(i)