def f(n):
    b = bin(n)[2:]
    d = b.count('1')
    b = b + str(d % 2)
    d = b.count('1')
    b = b + str(d % 2)
    return int(b,2)


print(f(13))

for i in range(1,1000):
    if f(i) < 50:
        print(f(i))