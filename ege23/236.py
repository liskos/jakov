def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 7:
        return 0
    if a % 10 == 7:
        return 0
    return f(a+1,b)+f(a+7,b)


print(f(1,61))