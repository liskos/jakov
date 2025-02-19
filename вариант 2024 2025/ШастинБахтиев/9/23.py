def f(a,b):
    if a==b:
        return 1
    if a < b:
        return 0
    if a == 26:
        return 0
    if a == 30:
        return 0
    return f(a-3,b)+f(a//2,b)


print(f(69,14))