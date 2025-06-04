import sys
sys.setrecursionlimit(100000)

def f(n):
    if n < 1000:
        return 66
    if n >= 1000:
        return f(n-5) + 100

print(f(180000)-f(100000))