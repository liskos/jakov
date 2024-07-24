def f(a,b,c=0):
    if a == b and c <= 5:
        return 1
    if a > b:
        return 0
    if a == 11 or a == 35:
        return 0
    if c == 5:
        return f(a+3,b,c)+f(a*2,b,c)
    return f(a+1,b,c+1)+f(a+3,b,c)+f(a*2,b,c)


print(f(2,18)*f(18,40))