def tr(n):
    t = "012345"
    s = ""
    while n > 0:
        s = t[n % 6] + s
        n //= 6
    return s


s = 6 ** 333 - 5 * 6 ** 215 + 3 * 6 ** 144 - 85
t = tr(s)
print(t.count('5'))
