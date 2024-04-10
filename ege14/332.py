def tr(n):
    t = "********8"
    s = ""
    while n > 0:
        s = t[n % 9] + s
        n //= 9
    return s


s = 19 ** 81 + 23 ** 709 - 4
t = tr(s)
print(t.count('8*'))
