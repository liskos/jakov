def f(a,b,k):
    if a == b:
        return 1
    if a > b:
        return 0

    if a % 2 == 0:
        k+=1
        return f(a+1,b,k)+f(a*2,b,k)+f(a+1,b,k)
    if a % 2 != 0:
        k+=1
        return f(a+1,b,k)+f(a*2,b,k)+f(a+2,b,k)


print(f(3,9,0)*f(9,17,0)*f(17,25,0))


