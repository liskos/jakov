def f(n):
    n = bin(n)[2:]
    n = n + n[-2]
    n = n + n[1]
    return int(n, 2)


k = 0
print(f(11))
for i in range(2,300):
    if 100 <= f(i) <= 150:
        k += 1
print(k)