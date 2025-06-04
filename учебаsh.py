def f(a,b,k=0):
    if a == b:
        return 1
    if a > b:
        return 0
    if k == 1:
        return f(a*3,b,k-1)
    return f(a+1,b)+f(a*2,b,k+1)+f(a*3,b)

print(f(8,123))