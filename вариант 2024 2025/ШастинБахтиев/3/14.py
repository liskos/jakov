def pr(n):
    s = ""
    t = "01234"
    while n > 0:
        s = t[n%5] + s
        n //= 5
    return s

for x in range(1,5556):
    s = 5 ** 150 + 5 ** 135 - x
    b = pr(s)
    if b.count("4") == 134:
        print(x)