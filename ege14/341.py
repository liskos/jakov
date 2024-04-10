def tr(n):
    t = "01234"
    s = ""
    while n > 0:
        s = t[n % 5] + s
        n //= 5
    return s


s = 4 * 625 ** 1920 + 4 * 125 ** 1930 - 4 * 25 ** 1940 - 3 * 5 ** 1950 - 1960
t = tr(s)
print(t.count('0'),t)
