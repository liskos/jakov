def f(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    return f(a-2,b)+f(a-4,b)+f(a**0.5,b)

print(f(46,32)*f(32,12)*f(12,2))
