import functools
@functools.lru_cache(None)
def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 11:
        return 0
    if a % 3 != 0:
        return f(a+1,b)+f(a*2,b)+f(a+a%3,b)
    return f(a+1,b)+f(a*2,b)

print(f(3,18))