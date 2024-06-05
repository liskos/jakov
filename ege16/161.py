import sys
sys.setrecursionlimit(1000000)
def f(n):
    if n < 10:
        return n
    if 10<=n<1000:
        return f(n//10)+f(n%10)
    if n >= 1000:
        return f(n//1000)-f(n%1000)


d = 0
for i in range(1,10**6+1):
    if f(i) == 0:
        d+=1
print(d)
