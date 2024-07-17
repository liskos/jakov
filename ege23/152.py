def f(a,b):
    if a == b:
        return 1
    if a> b:
        return 0
    return f(a+1,b)+f(a+2,b)


print(f(11,17)*f(17,29))
print(f(11,23)*f(23,29))
print(f(11,17)*f(17,23)*f(23,29))

print(3029*2-2197)