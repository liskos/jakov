def f(n):
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        n = int(n[:-1],2)
    else:
        n = int('1' + n + '00',2)

    return n


print(f(5))
for i in range(1,1000):
    if f(i) > 100:
        print(i)
        break