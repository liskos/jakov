def tr(n):
    t = "012345678"
    s = ""
    while n > 0:
        s = t[n % 9] + s
        n //= 9
    return s


s = 7 * 6561 ** 46 + 8 * 729 ** 15 - 6 * 5832
t = tr(s)
print(t.count('7'))