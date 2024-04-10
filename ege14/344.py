def tr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


s = 343 ** 1515 - 6 * 49 ** 1520 + 5 * 49 ** 1510 - 3 * 7 ** 1530 - 1550
t = tr(s)
print(t.count('0'),t)
