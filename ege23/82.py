def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 25:
        return 0
    return f(a+1,b)+f(a*2+1,b)


print(f(1,31))