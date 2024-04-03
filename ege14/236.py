def tr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


s = 8 * 343 ** 5 + 9 * 49 ** 8 - 48
t = tr(s)
print(t.count('6'))