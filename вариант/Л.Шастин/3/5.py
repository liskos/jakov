def d(n):
    t = "0123456789ab"
    s = ""
    while n > 0:
        s = t[n%12]+s
        n //= 12
    return s

def f(n):
    b = d(n)
    if n % 4 == 0:
        b = "2" + b + "64"
    else:
        b += "b"
    return int(b,12)

print(f(11),f(12))

for i in range(1,100):
    if f(i) > 1799:
        print(f(i))
        break