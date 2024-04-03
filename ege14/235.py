
def tr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


s = (2 * 343 ** 123 + 2401) * (3 * 343 ** 137 - 2401)
t = tr(s)
print(t.count('6'))