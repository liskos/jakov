def tr(n):
    t = "0123456789abcdefghjklmnop"
    s = ""
    while n > 0:
        s = t[n % 25] + s
        n //= 25
    return s


s = 13 * 625 ** 1320 + 12 * 125 ** 1230 - 14 * 25 ** 1140 - 13 * 5 ** 1050 - 2500
t = tr(s)
print(t.count('0'),t)
