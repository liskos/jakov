def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    z = [1,1,2,3,5,8,13,21]
    y = min([i for i in z if i > a])

    return f(a+1,b)+f(a+4,b)+f(y,b)


print(f(1,13))
