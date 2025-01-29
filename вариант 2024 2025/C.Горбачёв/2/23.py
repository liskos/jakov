def f(a,b,k=0):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 40:
        return 0
    if k > 0:
        return f(a+1,b,k-1)+f(a*a,b,k-1)
    return f(a+1,b,k)+f(a*2,b,k+1)+f(a*a,b,k)

print(f(5,80)*f(80,155))