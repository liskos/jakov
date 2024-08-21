def ch(n):
    t = "0123"
    s = ""
    while n>0:
        s = t[n%4] + s
        n //= 4
    return s

def f(n):
    b = ch(n)
    a = b[0]
    d = b[-1]
    if n % 3 == 0:
        b = d + b[1:-1] + a + "1"
    else:
        b = b + str(n % 3)
    return int(b,4)


print(f(11),f(13))

for i in range(1,10000):
    if f(i) <= 340:
        print(f(i))