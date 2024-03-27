def f(n):
    c = bin(n)[2:]
    if n % 2 == 0:
        b = c + '0'
    else:
        b = c + '1'
    if c.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'
    return int(b,2)

print(f(13))
for i in range(1,1000):
    if f(i) > 2023:
        print(f(i))