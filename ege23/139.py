
def chr(n):
    s = "0123"
    t = ""
    while n > 0:
        t = s[n%4]+t
        n //= 4
    return t
def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+2,b)+f(a+3,b)+f(int(chr(a)+"0",4),b)


a = int("1",4)
b = int("100",4)
print(f(a,b))

