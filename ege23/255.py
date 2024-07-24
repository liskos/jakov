def f(a,b,c=0):
    if a == b and c <= 3:
        return 1
    if a > b:
        return 0
    if a == 10 or a == 38:
        return 0
    if c == 3:
        return f(a+2,b,c)+f(a*3,b,c)
    return f(a+1,b,c+1)+f(a+2,b,c)+f(a*3,b,c)


print(f(2,25)*f(25,43))