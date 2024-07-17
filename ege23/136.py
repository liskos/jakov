def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1,b)+f(int("1"+ bin(a)[2:],2),b)


a = int("1",2)
b = int("11111",2)
print(f(a,b))

