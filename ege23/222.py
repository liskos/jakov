def f(a,b,z=0,x=0,c=0):
    if a == b:
        if z > 0 and x > 0 and c > 0:
            return 1
        else:
            return 0
    if a > b:
        return 0
    return f(a+1,b,z+1,x,c)+f(a+2,b,z,x+1,c)+f(a*2,b,z,x,c+1)


print(f(3,25))
