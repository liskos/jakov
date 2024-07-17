def f(a,b,c):
    if a == b:
        return 1
    if a > b :
        return 0
    if c:
        return f(a+1,b,False)+f(a*2,b,False)
    return f(a+1,b,False)+f(a+3,b,True)+f(a*2,b,False)


print(f(2,20, False))
