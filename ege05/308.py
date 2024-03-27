def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        d = ''.join('1' if n == '0' else '0' for b in b[-4:])
    else:
        d = b[:-4] + ''.join('1' if digit == '0' else '0' for digit in b[-4:])

    R = int(d, 2)

for i in range(1,1000):
    if i > 63:
        print(i,f(i))