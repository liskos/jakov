def f(a,b):
    if a == b or a == b + 1 or a == b + 2 or a == b + 3 or a == b + 4:
        return 1
    if a == 23:
        return 0
    if a > b:
        return 0
    return f(a+3,b)+f(a+4,b)+f(a*2,b)


print(f(11,50))