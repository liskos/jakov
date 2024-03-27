def f(n):
    b = bin(n)[2:]
    if n % 5 == 0:
        b = '1' + b + b[-2:]
    else:
        b = bin(n % 5)[2:] + b
    return int(b,2)


print(f(13))
print(f(10))
for i in range(2,1000):
    if 200 <= f(i) <= 223:
        print(f(i))