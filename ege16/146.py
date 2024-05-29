import functools,sys
sys.setrecursionlimit(10000)

def f(n):
    if n >= 10**4:
        return n
    if n < (10**4) and n % 4 == 0:
        return n/4 + f(n/4+2)
    if n < (10**4) and n % 4 != 0:
        return 1 + f(n+2)


print(f(174)-f(3))