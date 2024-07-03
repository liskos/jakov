def f(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    return f(a-8,b)+f(a//2,b)


print(f(102,43)*f(43,5))
