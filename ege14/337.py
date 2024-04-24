def tr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


s = 4 * 8 ** 3032 + 3 * 16 ** 1956 + 870
t = tr(s)
print(3*t.count('3') - t.count('1'))
