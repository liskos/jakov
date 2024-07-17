
def chr(n):
    s = "012"
    t = ""
    while n > 0:
        t = s[n%3]+t
        n //= 3
    return t
def f(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    if chr(a)[-1] == "0":
        return f(a-2,b)
    return f(a-2,b)+f(int(chr(a)[:-1]+"0",3),b)


a = int("212",3)
b = int("10",3)
print(f(a,b))

