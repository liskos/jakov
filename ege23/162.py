def f(a,b,count=0):
    if a == b:
        return 1
    if a > b or count >=2:
        return 0
    return f(a+1,b,0)+f(a+2,b,0)+f(a*2,b,0)

print(f(1,15))
