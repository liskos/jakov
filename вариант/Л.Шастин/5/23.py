def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 18 or a == 10:
        return f(a+2,b)+f(a*2,b)
    return f(a+2,b)+f(a+3,b)+f(a*2,b)


print(f(3,20))