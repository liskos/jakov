def tr(n):
    t = "012345678"
    s = ""
    while n > 0:
        s = t[n % 9] + s
        n //= 9
    return s


s = (729 ** 41 - 81 ** 16) * (729 ** 15 + 9 ** 5)
t = tr(s)
print(t.count('8'))