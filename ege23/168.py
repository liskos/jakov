
def f(a,b,count = 0):
    if a == b and count == 10:
        return 1
    if a > b and count != 10:
        return 0
    return f(a+4,b,count)+f(a+7,b,count)+f(a//2,b,count)

print(f(1,1))
