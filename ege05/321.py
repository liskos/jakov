def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b += bin(3)[2:]
    else:
        b += '1'
    if int(b,2) % 5 == 0:
        b += bin(5)[2:]
    else:
        b += '1'
    return int(b,2)

a = []
for i in range(10,1000000):
    if f(i) < 10**6:
        a.append(i)
print(max(a))
