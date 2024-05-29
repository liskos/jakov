import sys,functools
sys.setrecursionlimit(5000)
@functools.lru_cache(None)
def f(n):
    if n >= 5000:
        return n
    if 1<=n<=10000:
        return f(n+1)+f(n+2)


print(f(12345)*(f(10)-f(12))/f(11)+f(10101))