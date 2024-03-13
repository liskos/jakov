def f(n):
    b = sum(int(digit) for digit in str(n))
    b = bin(b)[2:]
    if b.count('0') % 2 == 0:
        b = '1' + b + '00'
    else:
        b = '10' + b + '1'
    return int(b,2)

print(f(123456789))
for i in range(1,1000):
    if f(i) == 21:
        print(i)