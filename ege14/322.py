def tr(n):
    t = "0123456789ab"
    s = ""
    while n > 0:
        s = t[n % 12] + s
        n //= 12
    return s


s = 12 ** 34 + 7 * 12 ** 26 - 3 * 12 ** 16 + 2 * 12 ** 5 + 552
t = tr(s)
t = set(t)
print(len(t))
