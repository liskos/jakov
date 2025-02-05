def dv(n):
    s = ""
    t = "0123456789abcdefghijklmno"
    while n > 0:
        s = t[n%25] + s
        n //= 25
    return s
a = []
for x in range(1,2501):
    s = 25 ** 150 + 25 ** 100 - x
    a.append(dv(s).count("0"))

for x in range(1,2501):
    s = 25 ** 150 + 25 ** 100 - x
    if dv(s).count("0") == max(a):
        print(x)