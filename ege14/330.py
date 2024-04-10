def tr(n):
    t = "0123456789abcdef"
    s = ""
    while n > 0:
        s = t[n % 16] + s
        n //= 16
    return s


s = 18 ** 105 + 25 * 16 ** 100 - 3 ** 51 + 15 ** 90
t = tr(s)
print(t.count('66'))
