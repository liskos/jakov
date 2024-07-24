
def f(a,b,c=False):
    if a == b:
        return 1
    if a > b :
        return 0
    if a == 12 or a == 20:
        return 0
    if c:
        return f(a+1,b,False)+f(a+2,b,False)
    return f(a+1,b,False)+f(a+2,b,False)+f(a*3,b,True)


print(f(2,15)*f(15,30)*f(30,38))

