def chr(n):
    s = ""
    t = "0123"
    while n > 0:
        s = t[n%4] + s
        n //= 4
    return s

b = []
for x in range(1,3000):
    s = 4 ** 210 + 4 ** 110 - x
    s = chr(s)
    if s.count("0") == 105:
        print(x)

print(max(b))