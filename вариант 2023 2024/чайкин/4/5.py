def pr(n):
    t = "01234"
    s = ""
    while n > 0:
        s = t[n%5] + s
        n //= 5
    return s

def f(s):
    b = pr(s)
    b = b[::-1]
    return int(b,5) - s

for i in range(1,10000):
    if f(i) == 100:
        print(i)