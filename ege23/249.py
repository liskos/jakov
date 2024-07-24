def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1
    if a == 58:
        return 0
    return f(a+1,b)+f(a+2,b)+f(a+3,b)+f(a*4,b)


print(f(38,45)*f(45,68))