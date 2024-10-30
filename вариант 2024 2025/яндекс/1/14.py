def five(n):
    v = ""
    t = "01234"
    while n > 0:
        v = t[n%5] + v
        n //= 5
    return v

for x in range(1,2042+1):
    s = 25 ** 61 + 5 ** 178 - x
    if (five(abs(s))).count("0") == 60:
        print(x)