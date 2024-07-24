
def f(a,b,c=False):
    if a == b:
        return 1
    if a > b :
        return 0
    if a == 30 or a == 40:
        return 0
    if c:
        return f(a+1,b,False)+f(a+3,b,False)
    return f(a+1,b,False)+f(a+3,b,False)+f(a*2,b,True)


print(f(3,20)*f(20,60))

