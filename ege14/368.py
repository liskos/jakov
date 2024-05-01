result = 0
for x in range(10):
    r1 = 12034 + x * 10
    r2 = 10234 + x * 1000
    n1 = r1 + 9
    n2 = 2 * r2 + 1
    n = n1 + n2
    if n % 11 == 0:
        result = n // 11
print(result)