def f(n):
    b = bin(n)[2:]
    c = b.count('1') % 2
    b = b + str(c)
    if b.count('1') > b.count('0'):
        b += '0'
    else:
        b += '1'
    return int(b,2)

for i in range(1,1000):
    if 50 <= f(i) <= 80:
        print(f(i))