
def f(a,b,k):
    if k == 4:
        return f(a+1,k+1)+f(a+5,k+1)+f(a*3,k+1)
        b.append(a)

print(f(1,0,0))