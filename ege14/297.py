def tr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


s = 7 ** 103 - 6 * 7 ** 70 + 3 * 7 ** 57 - 98
t = tr(s)
print(t.count('6'))
