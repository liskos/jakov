def f(a,b,s):
    if a + b == s:
        return 1
    if a + b > s:
        return 0
    return f(a+b,b,s)+f(a,a+b,s)


print(f(1,1,88))