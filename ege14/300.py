def tr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


s = 7 ** 103 + 20 * 7 ** 204 - 3 * 7 ** 57 + 97
t = tr(s)
print(t.count('6'))
