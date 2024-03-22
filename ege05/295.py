def f(n,m):
    b = bin(n)[2:]
    d = bin(m)[2:]
    s1 = b.count('1') ** 2
    s2 = d.count('1') ** 2
    s = s1 - s2
    return s


for i in range(1,1000):
    for b in range(1,1000):
        if f(i,b) == 33:
            print(i + b)