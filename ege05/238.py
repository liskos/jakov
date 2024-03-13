def f(n):
    d = str(n)
    b = int(str(n) + d[-1])
    b = bin(b)[2:]
    if b.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'
    return int(b,2)

print(f(13))

for i in range(1,1000):
    if f(i) > 413:
        print(i)
