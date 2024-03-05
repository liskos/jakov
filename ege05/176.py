def f(n):
    b = bin(n)[2:]
    a = b[0]
    b = b.replace('0','8')
    b = b.replace('1','0')
    b = b.replace('8','1')
    b = b[1:]
    b = a + b
    return int(b, 2) + int(n)



for i in range(1,1000):
    if f(i) < 123:
        print(i)

