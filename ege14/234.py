def tr(n):
    t = "012345678"
    s = ""
    while n > 0:
        s = t[n % 9] + s
        n //= 9
    return s


s = 5 * 6561 ** 46 + 5 * 729 ** 15 - 5 * 5832 - 5
t = tr(s)
print(t.count('4'))