def f(a, b, m2=0,ms=0):
    if a > b and m2 <= ms:
        return 0
    if a > b:
        return 0
    if a == b and m2 > ms:
        return 1
    else:
        return f(a+1,b,m2,ms+1)+f(a*2,b,m2+1,ms)+f(a*5,b,m2+1,ms)


print(f(3,260))