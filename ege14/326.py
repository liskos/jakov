def tr(n):
    t = "01234567"
    s = ""
    while n > 0:
        s = t[n % 8] + s
        n //= 8
    return s


s = 8 ** 888 + 16 * 16 * 1616 - 2 ** 444
t = tr(s)
print(t.count('7'))
