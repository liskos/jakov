import functools
@functools.lru_cache(None)

def f(n):
    if n < 2:
        return n
    if n >= 2 and n % 2 == 0:
        return f(n//2) + 1
    if n >= 2 and n % 2 != 0:
        return f(3*n+1)+1


h = 0
for i in range(1,100001):
    if f(i) == 16:
        h+=1

print(h)