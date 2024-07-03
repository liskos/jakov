def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1,b)+f(a+5,b)+f(a*3,b)


for i in range(1,100):
    if f(1,i)==175:
        print(i)
        break