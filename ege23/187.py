def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f()