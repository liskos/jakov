import  sys
sys.setrecursionlimit(1000000)
def f(n):
    if n < 100:
        return n
    if n >= 100:
        return n + f(n-2)


print(f(66666)/f(777))