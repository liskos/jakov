result = 0
for x in range(10):
    r1 = 12304 + x * 10
    r2 = 12340 + x
    n1 = r1 + 1
    n2 = r2 + 1
    n = n1 + n2
    if n % 10 == 0:
        result = n // 10
print(result)