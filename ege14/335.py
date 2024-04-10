def tr(n):
    t = "******6"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


s = 3 * 16 ** 2018 - 2 * 8 ** 1028 - 3 * 4 ** 1100 - 4 ** x - 2022
t = tr(s)
print(t.count('6*'))
