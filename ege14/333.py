def tr(n):
    t = "****4"
    s = ""
    while n > 0:
        s = t[n % 5] + s
        n //= 5
    return s


s = 81 ** 79 + 75 ** 2022 - 12 ** 35
t = tr(s)
print(t.count('4*'))
