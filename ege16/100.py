import functools
@functools.lru_cache(None)
def f(n):
    # if n == 0:
    #     return 0
    if n <= 3:
        return n + 3
    if n > 3 and f(n - 1) % 2 == 0:
        return f(n - 2) + n
    if n > 3 and f(n - 1) % 2 != 0:
        return f(n-2) + 2 * n


a = []
for i in range(40,51):
    a.append(f(i))
print(sum(a))