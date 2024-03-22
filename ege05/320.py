def f(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    if n % 2 == 0:
        s += '12'
    else:
        n += sum(map(int(s)))
        while n > 0:
            s += str(n % 3)
            n //= 3
    return int(s,3)


for i in range(1,1000):
    if f(i) < 15:
         print(i,f(i))