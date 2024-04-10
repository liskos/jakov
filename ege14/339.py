def tr(n):
    t = "012345"
    s = ""
    while n > 0:
        s = t[n % 5] + s
        n //= 5
    return s


s = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
t = tr(s)
print(sum(map(int,t)))
