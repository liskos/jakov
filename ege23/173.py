
def f(a,b,c):
    if a == b:
        return 1
    if a > b :
        return 0
    if a == 33:
        return 0
    if c:
        return f(a+1,b,False)+f(a+3,b,False)
    return f(a+1,b,False)+f(a+3,b,False)+f(a*2,b,True)


print(f(2,18,False)*f(18,51,False))

