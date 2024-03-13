def f(n):
    d = bin(n)[2:]
    c = d[0]
    b = d[1:]
    b = b.replace('0','8')
    b = b.replace('1','0')
    b = b.replace('8','1')
    b = c + b
    return int(b,2) + n


for i in range(1,1000):
    if f(i) > 99:
        print(i)
