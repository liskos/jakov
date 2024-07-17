def f(a,b,c):
    if a>b or (c % 2 != 0 and a % 2 != 0):
        return 0
    if a == b:
        return 1
    if a<b:
        return f(a+2,b,a)+f(a*3,b,a)+f(a*4,b,a)
print(f(1,600,0))