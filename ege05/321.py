def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b += bin(3)[2:]
    else:
        b += '1'
    if int(b,2) % 5 == 0:
        b += bin(5)[2:]
    else:
        b += '1'
    return int(b,2)


for i in range(4,1000):
    if f(i) < 10**6:
        print(i)