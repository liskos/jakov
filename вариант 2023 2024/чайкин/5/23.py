def f(a,b,k=0):
    if a == b and k == 3:
        return 1
    if a > b:
        return 0
    if a == 7 or a == 3 or a == 5 or a == 13 or a == 11 or a == 17 or a == 19 or a == 23 or a == 31:
        k+=1
    return f(a+1,b)+f(a+3,b)+f(a*2,b)

print(f(1,35))