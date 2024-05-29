import sys
sys.setrecursionlimit(100000)
import functools
@functools.lru_cache(None)
def f(n):
    if n < 4 or n % 2 != 0:
        return 1
    else:
        return f(n-1) + f(n-2) + f(n-3)

res = f(2008) - f(2006)
print(res)