import functools
import sys
sys.setrecursionlimit(10000)
@functools.lru_cache(None)
def f(n):
    if n <= 2:
        return 5
    else:
        return f(n-2) + n


print(f(23023))