import functools
@functools.lru_cache(None)
def F(n):
    if n == 0:
        return 1
    if n % 2 != 0:
        return 1 + F(n - 1)
    else:
        return F(n // 2)

count = 0
for n in range(1, 500000001):
    if F(n) == 3:
        count += 1

print(count)