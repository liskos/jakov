def tr(n):
    t = "012345678"
    s = ""
    while n > 0:
        s = t[n % 9] + s
        n //= 9
    return s


s = 7 * 729 ** 543 - 6 * 81 ** 765 - 5 * 9 ** 987 - 20
t = tr(s)
print(t.count('8'),t)
