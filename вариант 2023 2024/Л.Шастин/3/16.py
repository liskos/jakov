import functools,sys
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def f(n):
    if n < 10:
        return n
    if n >= 10:
        return g(f(n-1)%10)+f(g(n%10)-1)-f(n-3)
@functools.lru_cache(None)
def g(n):
    if n < 10:
        return -n
    if n >= 10:
        return f(g(n-1)%10)+g(f(n-1)-1)+g(n-2)


print(f(1111)+g(1111))