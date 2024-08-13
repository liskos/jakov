def f(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    if a == 13 and a == 15:
        return 0
    return f(a//3,b)+f(a-2,b)+f(a-5,b)


print(f(32,9))