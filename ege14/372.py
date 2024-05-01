result = 0
for x in range(10):
    r1 = int(f"12{x}34")
    r2 = int(f"1234{x}")
    n1 = 1 * r1 ** 1 + 9
    n2 = 2 * r2 ** 1 + 3
    n = n1 + n2
    if n % 10 == 0:
        print(n // 10)
