def f(a, b, m3=0,m5=0,s=0):
    if a > b or s > 5  or m5 > 4:
        return 0
    elif a == b and m5 <= 4 and m3 >= 2 and s == 5:
        return 1
    else:
        return f(a*5,b,m3,m5+1,s)+f(a*3,b,m3+1,m5,s)+f(a+45,b,m3,m5,s+1)


print(f(1,2970))