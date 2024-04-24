def tr(n):
    t = "01234"
    s = ""
    while n > 0:
        s = t[n % 5] + s
        n //= 5
    return s


s = 3 * 5 ** 1984 - 7 * 25 ** 777 - 11 * 125 ** 666 - 404
print(s)
t = tr(abs(s))
print(t)
print(t.count('2'))
