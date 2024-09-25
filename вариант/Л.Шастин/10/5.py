def d(n):
    s = ""
    t = "0123456789ab"
    while n > 0:
        s = t[n%12]+s
        n //= 12
    return s

def f(n):
    b = d(n)
    if n % 3 == 0:
        b = "1" + b + "b"
    else:
        b = "2" + b + "0"
    return int(b,12)

print(f(11),f(12))

for i in range(1,10000):
    if f(i) < 1996:
        print(f(i))