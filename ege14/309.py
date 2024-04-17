def tr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


s = 103 * 7 ** 103 - 5 * 7 ** 57 + 98
t = tr(s)
print(sum(map(int,t)))
