def tr(n):
    s = ""
    t = "012"
    while n > 0:
        s = t[n%3] + s
        n //= 3
    return s

def f(n):
    b = tr(n)
    if n % 2 == 0:
        b = b.replace("1","2")
        b += b[-2:]
    else:
        b = b + tr(n%3) + tr(n%3)
    return int(b,3)


print(f(11),f(16))

for i in range(1,100000):
    if f(i) <= 1165:
        print(i)
