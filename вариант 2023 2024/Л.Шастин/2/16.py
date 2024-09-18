import sys
sys.setrecursionlimit(10000)
def f(n):
    if n < 3:
        return 2 ** 1024
    if n > 2:
        return 2 * n + 3 + f(n-2)

print(f(4048)-f(16))