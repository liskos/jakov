def f(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    return f(a-3,b)+f(a-4,b)+f(a**0.5,b)

print(f(36,21)*f(21,3))
