def tr(n):
    t = "0123"
    s = ""
    while n > 0:
        s = t[n % 4] + s
        n //= 4
    return s


s = 4 ** 503 + 3 * 4 ** 244 - 2 * 4 ** 444 - 95
t = tr(s)
print(t.count('3'))
