def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = b.replace('1','',1)
    else:
        b = b.replace('1','') + '1'
    if b.count('1') % 2 == 0:
        b = b.replace('1','',1)
    else:
        b = b.replace('0','') + '1'
    return int(b,2)

print(f(5))

for i in range(5,1000):
    if f(i) == 7:
        print(i)