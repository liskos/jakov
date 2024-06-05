def F(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return F(n // 2)
    else:
        return F(n - 1) + 3

count = 0
for n in range(1, 1001):
    if F(n) == 18:
        count += 1

print(count)