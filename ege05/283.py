def f(n):
    b = bin(n)[2:]
    c = b.count('1')
    c = bin(c)[2:]
    if n % 2 == 0:
        b = b + c
    else:
        b = '1' + b + '00'
    return int(b,2)



for i in range(1,1000):
    if f(i) < 1000:
        print(i)
