import functools
@functools.lru_cache(None)
def f(n):
    if n <= 2 or n == 8:
        return 0
    if n == 3:
        return 1
    if n > 3 or n != 8:
        return f(n-2)+f(n-1)


for i in range(1,1000):
    if f(i) == 25:
        print(i)