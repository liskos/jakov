def f(n):
    b = bin(n)[2:]
    c = b.count('1')
    if n % 2 == 0:
        b = b + str(c)
    else:
        b = '1' + b + '00'
    return int(b,2)



for i in range(1,1000):
    if 500 <= f(i) <= 700:
        print(i)
