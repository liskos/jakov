def tr(n):
    t = "01234"
    s = ""
    while n > 0:
        s = t[n % 5] + s
        n //= 5
    return s


s = ((9 * 5 ** 20 + 9) * 5 ** 19 + 9) * 5 ** 18 + 9
t = tr(s)
print(t.count('0'), t.count('1'), t.count('2'), t.count('3'), t.count('4'))
