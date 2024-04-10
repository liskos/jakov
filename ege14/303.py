def tr(n):
    t = "0123"
    s = ""
    while n > 0:
        s = t[n % 4] + s
        n //= 4
    return s


s = 4 ** 1103 + 3 * 4 ** 1444 - 2 * 4 ** 144 + 66
t = tr(s)
print(int(sum(map(int,t),4)))
