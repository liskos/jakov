def f(n):
    b = bin(n)[2:]
    b = '0' * (8 - len(b)) + b
    b = b.replace('0', '8')
    b = b.replace('1', '0')
    b = b.replace('8', '1')
    return int(b, 2) + 1

print(f(221))

