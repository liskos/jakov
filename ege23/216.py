def f(a,b,l=0):
    if a == b:
        return 1
    if a > b:
        return 0
    k = f(a+1,a)+f(a*3,a)
    if l != 0:
        k+= f(a+l,a)
    return k

print(f(2,27))


