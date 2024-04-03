def tr(n):
    t = "012345"
    s = ""
    while n > 0:
        s = t[n % 6] + s
        n //= 6
    return s

s = (66 + 6 * 2019 + 66 + 6 ** 6)
t = tr(s)
print(sum(map(int,t)))