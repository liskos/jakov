def semb(n):
    s = ""
    t = "0123456"
    while n > 0:
        s = t[n%7] + s
        n //= 7
    return s

b = []
for x in range(1,2031):
    s = 7 ** 170 + 7 ** 100 - x
    b.append(semb(s).count("0"))


for x in range(1,2031):
    s = 7 ** 170 + 7 ** 100 - x
    if semb(s).count("0") == max(b):
        print(x)