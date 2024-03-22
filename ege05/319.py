def f(n):
    b = bin(n)[2:]
    if n % 10:
        b = b + b[-4] + b[-3] + b[-2] + b[-1]
        return int(b,2)
    else:
        c = int(b[-1]) ** 2 // 2
        c = bin(int(b))[2:]
        c = b + c
        return int(c,2)


k=0
for i in range(11,1000):
    if f(i) < 680:
        k+=1
print(k)