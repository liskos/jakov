import sys
sys.setrecursionlimit(100000)

def f(n):
    if n>= 2025:
        return n
    if n < 2025:
        return f(n+1)-f(n+2)+7


print(f(15)-f(24))