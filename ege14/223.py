def tr(n):
    t = "01234"
    s = ""
    while n > 0:
        s = t[n % 5] + s
        n //= 5
    return s

s = 4**4 * 5**69 - 70
t = tr(s)
print(t.count('0'),t.count('1'),t.count('2'),t.count('3'),t.count('4'))