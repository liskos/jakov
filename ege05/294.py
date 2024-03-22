def f(n):
    b = list(str(n))
    if n % 2 == 0:
        b.sort(reverse=True)
        b = int(''.join(b))
        b //= 2
    else:
        b = sorted(b)
        b = int(''.join(b))
        b *= 2
    return b


print(f(1488))
for i in range(1000,10000):
    if f(i) == i + 1:
        print(f(i))
        break