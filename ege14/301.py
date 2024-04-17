def tr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


n = 7 ** 103 + 6 * 7 ** 104 - 3 * 7 ** 57 + 98
s = tr(n)
print(sum(map(int,s)))
