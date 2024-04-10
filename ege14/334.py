def tr(n):
    t = "******6"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


s = 53 ** 123 + 65 ** 2222 - 172 ** 12
t = tr(s)
print(t.count('6*'))
