def tr(n):
    t = "0******7"
    s = ""
    while n > 0:
        s = t[n % 8] + s
        n //= 8
    return s


s = 8 ** 888 + 15 * 15 ** 1515 - 2 ** 444
t = tr(s)
print(t)
print(t.count('7*'))
