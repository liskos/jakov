import sys,functools
sys.setrecursionlimit(10000)
@functools.lru_cache(None)
def f(n):
    if n == 1025:
        return 1
    return f(n-1) * (3**((n%5)-(n%7)))

print(f(1025)/(f(1030)))
