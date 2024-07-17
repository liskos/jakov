def f(a, b, m2=0):
    if a > b or m2 > 3:
        return 0
    if a == b and m2 <= 3:
        return 1
    else:
        return f(a+2,b,m2)+f(a*3,b,m2+1)+f(a*5,b,m2+1)


print(f(2,200))