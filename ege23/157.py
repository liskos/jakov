def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 12:
        return 0
    p = 1
    for x in range (1,a+2):
        p = p * x
    return f(a+1,b)+f(a+4,b)+f(p,b)


print(f(2,24))
