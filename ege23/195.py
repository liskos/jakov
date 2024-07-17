def f(a, b, m2=0):
    if a > b or m2 > 2:
        return 0
    if a == b and m2 <= 2:
        return 1
    else:
        return f(a+1,b,m2)+f(a*2,b,m2+1)+f(a*3,b,m2+1)


print(f(1,100))