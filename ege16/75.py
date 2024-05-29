import functools
import sys
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def f(n):
    if n <= 1:
        return n
    if n > 1 and n % 2 == 0:
        return 1 + f(n // 2)
    if n > 1 and n % 2 != 0:
        return 1 + f(n+2)

for i in range(1,10000000000):
    if f(i) == 16:
        print(f(i))


