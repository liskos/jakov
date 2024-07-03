def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1,b)+f(int(bin(a)[2:]+"0", 2),b) + f(int(bin(a)[2:]+"1",2),b)

v = int("100",2)
z = int("11101",2)
print(f(v,z))


