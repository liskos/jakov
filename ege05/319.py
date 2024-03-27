def f(n):
    b = bin(n)[2:]
    if n % 10 == 0:
        c = b + b[-4:]
    else:
        c = int(str(n)[-1]) ** 2 // 2
        c = bin(c)[2:]
        c = b + c
    return int(c,2)

print(f(20))
k=0
for i in range(11,10000):
    if f(i) < 680:
        k+=1
print(k)