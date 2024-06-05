import functools
@functools.lru_cache(None)
def f(n):
    if n > 1000000:
        return n
    if n <= 1000000:
        return n + f(3*n)

import functools
@functools.lru_cache(None)
def g(n):
    return f(n)//n

d = 0
for i in range(1,1000000):
    if g(i) == 1000:
        d+=1

print(d)