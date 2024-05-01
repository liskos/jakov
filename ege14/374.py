result = 0
for x in range(10):
    r1 = 10234 + x * 1000
    r2 = 10243 + x * 1000
    n1 = r1 ** 2 + r1 + 2
    n2 = r2 ** 2 + r2 + 1
    n = n1 + n2
    if n % 15 == 0:
        result = n // 15
print(result)