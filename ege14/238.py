def tr(n):
    t = "01234567"
    s = ""
    while n > 0:
        s = t[n % 8] + s
        n //= 8
    return s


s = (512 ** 78 - 512 ** 60) * (512 ** 5 + 64 ** 5)
t = tr(s)
print(t.count('7'))