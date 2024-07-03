def f(a,b,k):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a*2,b,k+1)+f(a*2+1,b,k+1)

for i in range(1,1000):
    if f(1,i,0)


