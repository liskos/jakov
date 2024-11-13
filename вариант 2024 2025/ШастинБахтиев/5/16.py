import sys
sys.setrecursionlimit(10000)
def f(n):
    if n > 3000:
        return n
    if n <= 3000:
        return (2 * n + 4) * f(n+2)

x = int(f(20)/f(28))
print(sum(map(int,str(x))))