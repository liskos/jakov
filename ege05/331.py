def f(n):
    b = bin(n)[2:]
    if n % 2 != 0:
        b = b.replace('1','8')
        b = b.replace('0','1')
        b = b.replace('8','0')
    d = ''
    for i in b:
        d += i * 2
    return int(d,2)

print(f(5))
for i in range(1,1000):
    if f(i) > 60:
        print(i)