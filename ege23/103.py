def f(a,b,k):
    if a == b:
        if k == 6:
            return 1
        else:
            return 0
    if a > b:
        return 0
    k+=1
    return f(a+1,b,k)+f(a+2,b,k)+f(a*2,b,k)

print(f(1,20,0))


