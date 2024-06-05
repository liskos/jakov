import functools,sys
sys.setrecursionlimit(1000000000)
@functools.lru_cache(None)
def f(n):
    if n == 0:
        return 0
    return f(n-1) + 2 * n


d = 0
for i in range(100000000,200000000):
    if f(i) % 3 != 0:
        d += 1
print(d)