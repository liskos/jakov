def f(a,b):
    if a == b:
        return 1
    if a == 20:
        return 0
    if a < b:
        return 0
    return f(a-1,b)+f(a-2,b)+f(a**0.5,b)

print(f(27,18)*f(18,6))
