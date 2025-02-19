def sem(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n%7] + s
        n //= 7
    return s

b = []
for x in range(1,10001):
    s = 7 ** 270 + 7 ** 170 + 7 ** 70 - x
    s = sem(s)
    b.append(s.count("0"))

for x in range(1,10001):
    s = 7 ** 270 + 7 ** 170 + 7 ** 70 - x
    s = sem(s)
    if s.count("0") == max(b):
        print(x)