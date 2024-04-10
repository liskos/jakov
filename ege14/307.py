def tr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


s = 7 ** 1003 + 6 * 7 ** 1104 - 3 * 7 ** 57 + 294
t = tr(s)
print(int(sum(map(int,t),7)))
