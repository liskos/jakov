def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 30:
        return 0
    return f(a+1,b)+f(a*2,b)+f(a*3,b)


print(f(10,60)*f(60,70))

print(40)