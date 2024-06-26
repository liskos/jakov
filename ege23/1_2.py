def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    if b % 2 == 0:
        return f(a,b - 1)+f(a,b // 2)
    return f(a, b-1)


print(f(1,16))