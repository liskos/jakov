def tr(n):
    t = "012"
    s = ""
    while n > 0:
        s = t[n % 3] + s
        n //= 3
    return s


s = 81 ** 18 - (81 ** 8 - 1)*((8 + 1) ** 8 + 1)//8 - 8
t = tr(s)
print(t.count('1'))