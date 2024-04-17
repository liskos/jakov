def tr(n):
    t = "012345"
    s = ""
    while n > 0:
        s = t[n % 6] + s
        n //= 6
    return s


s = 6 ** 1333 - 5 * 6 ** 1215 + 3 * 6 ** 144 - 86
t = tr(s)
print(sum(map(int,t)))
