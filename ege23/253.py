def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 2 or a == 3 or a == 5 or a == 7 or a == 11 or a == 13 or a == 17 or a == 19 or a == 23 or a == 29 or a == 31:
        return 0
    return f(a+1,b)+f(a+2,b)+f(a*3,b)


print(f(8,16)*f(16,32))
