def f(n):
    b = bin(n)[2:]
    h = sum(int(d)for d in b)
    if h % 4 == 0:
        b = '10' + b
    else:
        b = '11' + b
    s = '0' if int(b,2) % 2 != 0 else '1'
    b = b + s
    return int(b,2)


for i in range(1,1000):
    if f(i) <= 250:
        print(i)