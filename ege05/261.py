def f(n):
    b = bin(n)[2:]
    c = b[0] + b[1]
    if b.count('0') > 0:
        b = b[:-1]
        b = b + c
        b = b[::-1]
        return int(b,2)
    else:
        return int(b,2)


for i in range(2,1000):
    if f(i) == 127:
        print(i)