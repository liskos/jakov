import functools
@functools.lru_cache(None)
def f(n):
    if n < 9:
        return n // 3 + n % 3
    if n >= 9:
        return f(n//9)+f(n%9)

d = 0
for i in range(1,9**9+1):
    if f(i) == 33:
        d+=1
print(d)