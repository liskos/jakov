def f(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    return f(a-1,b)+f(int(bin(a)[2:-1],2),b)


v = int("110",2)
z = int("110111",2)
print(f(z,v))

