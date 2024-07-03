def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 21:
        return 0
    if a % 2 == 0:
        return f(a+1,b)+f(a+4,b)+f(a+(a+2),b)
    if a % 2 != 0:
        return f(a+1,b)+f(a+4,b)+f(a+(a+1),b)


print(f(2,11)*f(11,26))
