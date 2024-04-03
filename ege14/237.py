def tr(n):
    t = "012345"
    s = ""
    while n > 0:
        s = t[n % 6] + s
        n //= 6
    return s


s = 7 * 1296 ** 57 - 8 * 216 ** 30 + 35
t = tr(s)
print(t.count('5'))