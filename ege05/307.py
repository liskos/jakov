def f(n):
    b = bin(n)[2:]
    n = n - b.count('0')
    n = bin(n)[2:]
    n = n[-3] + n[-2] + n[-1] + n
    return int(n,2)

print(f(13))

for i in range(5,1000):
    if f(i) > 224 and f(i) < 230:
        print(f(i))
