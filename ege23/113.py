from functools import *
@cache
def f(a,b,k):
    c = []
    if a == b:
        return 1

    if a > b:
        return 0

    return f(a+1,b,k+1)+f(a+2,b,k+1)+f(a*3,b,k+1),c.append(k)

print(f(1,227,0))


