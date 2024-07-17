def f(a,c=0):
    if c > 7:
        return 0
    if a == 10 and c <= 7:
        return 1
    return f(a+1,c+1)+f(a*2,c+1)+f(a-3,c+1)
print(f(1))


