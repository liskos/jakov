def f(n):
    n = bin(n)[2:]
    b = str(n)
    n = str(n) + b[-2]
    n = str(n) + b[1]
    return int(n, 2)


k = 0
print(f(11))
for i in range(2,201):
    if 150 <= f(i) <= 200:
        k += 1
print(k)