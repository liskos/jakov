import functools
import sys
sys.setrecursionlimit(10000)
@functools.lru_cache(None)
def f(n):
    if n <= 400:
        return 1
    else:
        return f(n-1)*(n-400)


print(f(701)/f(697))