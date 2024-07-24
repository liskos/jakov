def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 6:
        return 0
    if a == 16:
        return 0
    if a == 26:
        return 0
    if a == 36:
        return 0
    return f(a+1,b)+f(a+3,b)


print(f(1,45))