def f(n):
    n = bin(n)[2:]
    n = int(n) + int(n) % 2
    n = str(n)
    if n.count('1') % 2 == 0:
        r = n + '0'
    else:
        r = n + '1'
    r = n
    if n.count('1') % 2 == 0:
        r = n + '0'
    else:
        r = n + '1'
    return int(r,2)



for i in range(114,10000):
    if f(i) > 114:
        print(f(i))
        break

