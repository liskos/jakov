def tr(n):
    t = "0123"
    s = ""
    while n > 0:
        s = t[n % 4] + s
        n //= 4
    return s


s = (64 ** 25 + 4 ** 10) - (16 ** 20 + 32 ** 3)
t = tr(s)
print(t[-20:])
