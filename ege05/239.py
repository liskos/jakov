def f(n):
    c = str(n)
    b = int(c + c[-1])
    b = bin(b)[2:]
    b = b + b[-1]
    return int(b,2)
print(f(13))

for i in range(1,1000):
    if f(i) > 413:
        print(i)
