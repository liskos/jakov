from functools import cache
@cache
def f(a,b,c=0,d=0):
    if a > b:
        return 0
    if a == b:
        return 1
    if c == 1:
        return f(a*2,b,c-1,d+1)+f(a*3,b,c-1,d+1)
    if d == 1:
        f(a + 1, b, c + 1, d-1) + f(a + 2, b, c + 1, d-1)
    return f(a+1,b,c+1,d)+f(a+2,b,c+1,d)+f(a*2,b,c,d+1)+f(a*3,b,c,d+1)


print(f(1,55555))