def f(a,b):
    if a == b:
        return 1
    if a == 27:
        return 0
    if a > b:
        return 0
    return f(a+3,b)+f(a+5,b)+f(a*a,b)

print(f(3,16)*f(16,51))