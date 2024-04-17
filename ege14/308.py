def tr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


s = 6 * 343 ** 1156 - 5 * 49 ** 1147 + 4 * 7 ** 1153 - 875
t = tr(s)
print(sum(map(int,t)))
