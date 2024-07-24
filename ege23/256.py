def f(a,b,c=0):
    if a == b and c <= 6:
        return 1
    if a > b:
        return 0
    if a == 20 or a == 58:
        return 0
    if c == 6:
        return f(a+3,b,c)+f(a*3,b,c)
    return f(a+1,b,c+1)+f(a+3,b,c)+f(a*3,b,c)


print(f(3,37)*f(37,95))