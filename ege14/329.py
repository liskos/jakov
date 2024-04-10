def tr(n):
    t = "012345678"
    s = ""
    while n > 0:
        s = t[n % 9] + s
        n //= 9
    return s


s = 9 ** 81 + 27 ** 729 - 4
t = tr(s)
t = t.replace('0','8')
print(t.count('8'))
