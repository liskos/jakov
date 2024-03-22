def f(n):
    b = list(str,(n))
    if n % 2:
        b = b.sorted(reverse=True)
        num = int(''.join(map(str, b)))
        num //= 2
    else:
        b = b.sorted
        b *= 2


print(f(1488))
for i in range(10,10000):
    if f(i) > f(756) + 1:
        print(f(i))