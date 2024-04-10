def tr(n):
    t = "012345678"
    s = ""
    while n > 0:
        s = t[n % 9] + s
        n //= 9
    return s


s = 3 ** 72 + 6 * 3 ** 50 - 7 * 3 ** 26 + 2 * 3 ** 15 + 155
t = tr(s)
t = set(t)
print(len(t))
