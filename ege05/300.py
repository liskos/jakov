def f(n):
    b = bin(n)[2:]
    b = b.replace('1','',1)
    if b.count('1') % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '0'
    return int(b,2)


for i in range(1,10000):
    if f(i) < 450:
        print(f(i))