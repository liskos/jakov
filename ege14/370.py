result = 0
for x in range(10):
    r1 = 12340 + x
    r2 = 12034 + x * 100
    n1 = r1 + 5
    n2 = r2 + 5
    n = n1 + n2
    if n % 14 == 0:
        result = n // 14
print(result)