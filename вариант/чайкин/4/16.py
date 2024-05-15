import functools


@functools.lru_cache(None)
def f(n):
    if n < 3:
        return n
    if n > 2:
        return (2*n-1)*(f(n-1)+f(n-2))


print(f(69)%(10**9+7))
