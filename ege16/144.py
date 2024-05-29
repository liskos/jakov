import sys
sys.setrecursionlimit(5000)
import functools
@functools.lru_cache(None)
def f(n):
    if n >= (10**4):
        return n
    if (n < 10**4) and n % 2 == 0:
        return 1 + f(n//2)
    if (n < 10**4) and n % 2 != 0:
        return (n ** 2) + f(n+2)

print(f(192)-f(9))
