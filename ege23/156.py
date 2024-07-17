def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    p = 1
    for x in range (1,a+1):
        p = p * x
    return f(a+1,b)+f(a+4,b)+f(a+p,b)


print(f(1,10)*f(10,20))
