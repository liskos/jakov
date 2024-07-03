def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+2,b)+f(a+5,b)

for i in range(1,1000):
    if f(5,i) == 34:
        print(i)