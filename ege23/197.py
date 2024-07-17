def f(a, b, m2=0):
    if a > b or m2 > 5:
        return 0
    if a == b and m2 <= 5:
        return 1
    else:
        return f(a+1,b,m2)+f(a*3,b,m2+1)+f(a*4,b,m2+1)


print(f(3,300))