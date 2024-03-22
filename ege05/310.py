def f(n):
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        n = '11' + n[2:] + '00'
    else:
        n = '10' + n[2:] + '11'
    if n.count('1') % 2 == 0:
        n = '11' + n[2:] + '00'
    else:
        n = '10' + n[2:] + '11'
    return int(n,2)

for i in range(1,1000):
    if f(i) < 1500:
        print(f(i))