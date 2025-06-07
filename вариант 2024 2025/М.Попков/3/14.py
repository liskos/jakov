def p(n):
    n = abs(n)
    s = ""
    t = "01234"
    while n > 0:
        s = t[n%5] + s
        n //= 5
    return s

b = []
for x in range(1,2006):
    s = 5 ** 150 + 5 ** 98 - x
    s = p(s)
    b.append(s.count("0"))

for x in range(1,2006):
    s = 5 ** 150 + 5 ** 98 - x
    s = p(s)
    if s.count("0") == max(b):
        print(x)