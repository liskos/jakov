import functools,sys
sys.setrecursionlimit(10000)

def f(n):
    if n >= 10**4:
        return n
    if n < (10**4) and n % 2 == 0:
        return f(n+1)+ n ** 2 - 3*(n-1)
    if n < (10**4) and n % 2 != 0:
        return f(n+2)+5*n-(n-1)


print(f(9950)-f(9999))