def tr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


s = 12 * 7 ** 135 + 11 * 7 ** 92 - 63 * 7 ** 22 + 17 * 7 ** 11 + 157
t = tr(s)
t = set(t)
print(len(t))
