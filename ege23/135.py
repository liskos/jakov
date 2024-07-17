def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1,b)+f(int("1"+ bin(a)[2:],2),b)


a = int("100",2)
b = int("110001",2)
print(f(a,b))

