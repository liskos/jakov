import functools
@functools.lru_cache(None)

def f(n):
    b = sum(map(int,str(n)))
    if n == 0:
        return 0
    if n < 3:
        return 1
    if n > 2 and b % 2 == 0:
        return f(n-1)-f(n-2)
    if n > 2 and b % 2 != 0:
        return f(n-1)+f(n//2)

print(f(100))