def f(n):
    b = bin(n - 1)[2:]
    b = '0' * (8 - len(b)) + b
    b = b.replace('0', '8')
    b = b.replace('1', '0')
    b = b.replace('8', '1')
    return int(b, 2)


print(f(204))
for i in range(1,128):
    if i == 178:
        print(f(i))

