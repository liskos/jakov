result = 0
for x in range(10):
    r1 = 12305 + x * 10
    r2 = 10233 + x * 1000
    n1 = r1 + 5
    n2 = r2 + 5
    n = n1 + n2
    if n % 14 == 0:
        result = n // 14
print(result)