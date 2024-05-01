result = 0
for x in range(10):
    r1 = 10234 + x * 1000
    r2 = 1234 + x * 10000
    n1 = r1 + 3
    n2 = r2 + 3
    n = n1 + n2
    if n % 13 == 0:
        result = n // 13
print(result)