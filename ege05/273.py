def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '11' + b + '11'
    else:
        b = '1' + b + '0'
    return int(b,2)
print(f(14))

for i in range(1,1000):
    if f(i) < 126:
        print(f(i))