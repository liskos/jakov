def tr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


s = 49 ** 129 + 7 ** 131 - 2
t = tr(s)
t = t.replace('0','6')
print(t.count('6'))
