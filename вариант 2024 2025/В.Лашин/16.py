import sys
sys.setrecursionlimit(3000)
def f(n):
    if n < 2:
        return n ** 2
    if n >= 2:
        return 2 * n * f(n-1)

print(f(2002)/f(2000))