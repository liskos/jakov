def tr(n):
    s = ""
    t = "012"
    while n > 0:
        s = t[n%3] + s
        n //= 3
    return s


def f(n):
    b = tr(n)
    b = b.replace("0","8").replace("2","0").replace("8","2")
    b = int(b)
    b = str(b)
    return abs(n - int(b,3))

for i in range(1,10000000):
    if f(i) == 1864246:
        print(i)
        break