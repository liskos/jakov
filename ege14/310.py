def tr(n):
    t = "012345"
    s = ""
    while n > 0:
        s = t[n % 6] + s
        n //= 6
    return s


s = 5 * 216 ** 1256 - 5 * 36 ** 1146 + 4 * 6 ** 1053 - 107
t = tr(s)
t = sum(map(int,t))
t = int(t,10)
print(t)