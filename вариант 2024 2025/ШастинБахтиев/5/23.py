def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+3,b)+f(a+int(max(str(a))),b)


print(f(10,24)*f(24,41))