def f(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    if a == 24:
        return 0
    return f(a-3,b)+f(a//3,b)

print(f(308,81)*f(81,5))