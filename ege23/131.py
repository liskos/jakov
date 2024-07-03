def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1,b)+f(int(str(a)+"0",b))+f(int(str(a)+"1",b))

v = int("100",2)
z = int("11101",2)
print(f(v,z))


