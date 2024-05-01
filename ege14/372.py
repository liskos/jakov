result = 0
for x in range(10):
    r1 = 12034 + x * 100
    r2 = 12403 + x * 10
    n1 = r1 ** 2 + 1
    n2 = r2 ** 2 + r2 + 1
    n = n1 + n2
    if n % 30 == 0:
        result = n // 30
print(result)