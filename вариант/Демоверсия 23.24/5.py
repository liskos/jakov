def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b += b[-3:]
    else:
        b += bin((n % 3)*3)[2:]
    return int(b,2)

print(f(12),f(4))

for i in range(1,1500):
    if f(i) > 151:
        print(f(i))
        break