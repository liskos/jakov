def f(a,b,k=0):
    if a == b and k < 6:
        return 1
    if a > b or k >= 6:
        return 0
    return f(a+1,b,k+1)+f(a*2,b,k+1)

for x in range(4, 100):
    print(x, f(3,x))