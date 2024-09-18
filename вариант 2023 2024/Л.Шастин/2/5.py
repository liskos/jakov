def sr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n%7] + s
        n //= 7
    return s

def f(n):
    b = sr(n)
    if b.count("2") % 2 == 0:
        b += "555"
    else:
        b = "1" + b
    return int(b,7)


print(f(11))
print(f(14))
for i in range(1,100000):
    if f(i) < 3799:
        print(i)
