result = 0
for x in range(10):
    r1 = 12304 + x * 10
    r2 = 12403 + x * 10
    n1 = r1 ** 2 + r1 + 3
    n2 = r2 ** 2 + 2 * r2 + 2
    n = n1 + n2
    if n % 10 == 0:
        result = n // 10
print(result)