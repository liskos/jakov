def f(a,b,c):
    if a>b:
        return 0
    if sum(map(int,str(a))) == 14:
        c+=1
    if a == b and c == 5:
        return 1
    return f(a+2,b,c)+f(a*3,b,c)+f(a*4,b,c)
print(f(1,600,0))