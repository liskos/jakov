
def f(a,b,k=0):
    if a == b:
        if k % 2 == 1:
            return 1
    if a > b:
        return 0
    return f(a+2,b,k+1)+f(a*2,b,k+1)+f(a*a,b,k+1)

print(f(1,100))
