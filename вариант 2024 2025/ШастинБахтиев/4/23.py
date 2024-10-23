def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 6:
        return f(a + 2, b) + f(a + 5, b)
    return f(a+2,b)+f(a+5,b)+f(a*a,b)

print(f(4,36))