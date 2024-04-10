def tr(n):
    t = "0123456789a"
    s = ""
    while n > 0:
        s = t[n % 11] + s
        n //= 11
    return s


s = 3 * 11 ** 58 + 15 * 11 ** 55 - 99 * 11 ** 18 + 125 * 11 ** 9 + 381
t = tr(s)
t = set(t)
print(len(t))
