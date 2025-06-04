def chr(n):
    n = abs(n)
    s = ""
    t = "0123"
    while n > 0:
        s = t[n%4] + s
        n //= 4
    return s
print(4**8+4**5 + int("300000000", 4))
s = 4 ** 8 + 4 ** 5
m = 12
z = 0
for x in range(1,500000):
    s1 =  s - x
    b = chr(s1)
    if b.count("0") == 8:
        if len(b) <= m:
            m = len(b)
            z = x
print(m)

print(z)
